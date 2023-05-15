import uvicorn
import torch
import pandas as pd
from fastapi import FastAPI, Request
from model import SentenceTransformerMulti
from utils import *
import redis
import faiss
import numpy as np
import collections, functools, operator
from opensearch_dsl import Search
from dotenv import load_dotenv

load_dotenv('.env')
HOST_EMB = os.getenv('HOST_EMB')
HOST_REDIS = os.getenv('HOST_REDIS ')
OPENSEARCH_INDEX = os.getenv('OPENSEARCH_INDEX')

def checkGPU():
    if torch.cuda.is_available():
        print("Cuda GPU available")
        print(torch.cuda.device_count(), "Devices")
        print("Current device:")
        print(torch.cuda.get_device_name(0))

    elif torch.backends.mps.is_available():
        print("Mac M1 acceleration available!")


PATH_HEADERS_INDEX = "./index_data/headers.index"
PATH_CONTENT_INDEX = "./index_data/content.index"
app = FastAPI()

print('\n\n')
print('='*100)
print('Starting Embeddings Service.....')
checkGPU()
model = SentenceTransformerMulti()
print('Embeddings Service Started')
print('='*100)
print('\n\n')

# Load faiss indexes
header_index = loadIndex(PATH_HEADERS_INDEX)
if not header_index:
    header_index = createIndex(model.dimensions)

content_index = loadIndex(PATH_CONTENT_INDEX)
if not content_index:
    content_index = createIndex(model.dimensions)

# Load redis
r_headers = redis.Redis(host=HOST_REDIS, port=6379, db=1)
r_content = redis.Redis(host=HOST_REDIS, port=6379, db=2)

# Load opensearch
opensearch_client = initOpenSearch()

@app.post("/getEmbeddings/")
async def getEmbeddings(request: Request):
    response = await request.json()
    data = model.getEmbedding(response['data'])
    return {'emb': data.tolist()}

@app.post("/search/")
async def getEmbeddings(request: Request):
    response = await request.json()

    # Context
    resp = opensearch_client.search(index=OPENSEARCH_INDEX, size=1000, body={"query":{
        "match": {
            "title": {
                "query": response['context'],
                "fuzziness": "auto"
                }
            }
        }
    })

    ids = [o['_id'] for o in resp['hits']['hits']]

    # Search config
    k = 100
    alpha = 0.65
    # Headers
    emb_headers = model.getEmbedding(response['headers'])
    faiss.normalize_L2(emb_headers)

    D, I = header_index.search(emb_headers, k)  # search

    dics_headers = []
    for i, index_header in enumerate(I):
        aux = {}
        for j, res in enumerate(index_header):
            id = r_headers.get(str(res)).decode("utf-8")
            # Check if same context
            if id in ids:
                aux[id] = D[i][j]
        dics_headers.append(aux)

    avg_headers = dict(functools.reduce(operator.add,
         map(collections.Counter, dics_headers)))
    n_columns = len(response['headers'])
    avg_headers = {key: (avg_headers[key] / n_columns)*alpha
                        for key in avg_headers.keys()}

    # Content
    emb_content = model.getEmbedding(response['content'])
    faiss.normalize_L2(emb_content)

    D, I = content_index.search(emb_content, k)  # search

    dics_content = []
    for i, index_content in enumerate(I):
        aux = {}
        for j, res in enumerate(index_content):
            id = r_content.get(str(res)).decode("utf-8")
            # Check if same context
            if id in ids:
                aux[id] = D[i][j]
        dics_content.append(aux)

    avg_content = dict(functools.reduce(operator.add,
         map(collections.Counter, dics_content)))
    avg_content  = {key: (avg_content[key] / n_columns) *(1-alpha)
                        for key in avg_content.keys()}

    total = dict(functools.reduce(operator.add,
         map(collections.Counter, [avg_content,avg_headers])))

    total_sorted = dict(sorted(total.items(), key=lambda item: item[1], reverse=True))
    results = []
    # Metadata retrieval
    for key, val in total_sorted.items():
        s = Search(using=opensearch_client, index=OPENSEARCH_INDEX) \
                .query("match", _id=key)

        response = s.execute()
        response[0]._d_['score'] = round(val, 2)
        results.append(response[0]._d_)
    return {'results': results}


@app.post("/index/")
async def indexDataset(request: Request):
    response = await request.json()
    table = pd.read_json(response['data'], orient='split')
    headers = cleanHeaders(table)
    content = cleanContent(table)

    headers_emb = model.getEmbedding(headers)
    content_emb = model.getEmbedding(content)

    faiss.normalize_L2(headers_emb)
    faiss.normalize_L2(content_emb)

    for emb in headers_emb:
        id = header_index.ntotal + 1
        header_index.add_with_ids(np.array([emb]), id)
        r_headers.set(str(id), response['id'])

    for emb in content_emb:
        id = content_index.ntotal + 1
        content_index.add_with_ids(np.array([emb]), id)
        r_content.set(str(id), response['id'])

    return {'index': 'ok'}


@app.get("/saveIndexes/")
async def saveIndexes():
    faiss.write_index(header_index, PATH_HEADERS_INDEX)
    faiss.write_index(content_index, PATH_CONTENT_INDEX)

    return {"index": "saved"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
