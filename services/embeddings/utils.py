import faiss
import os
import json
from opensearchpy import OpenSearch, RequestsHttpConnection
from dotenv import load_dotenv

load_dotenv('.env')

# OpenSearch Config
OPENSEARCH_HOST = os.getenv('OPENSEARCH_HOST')
OPENSEARCH_INDEX = os.getenv('OPENSEARCH_INDEX')
USERNAME = os.getenv('OPENSEARCH_USERNAME')
PASS = os.getenv('OPENSEARCH_PASS')
auth = (USERNAME, PASS)


def saveIndex(index, filename):
    faiss.write_index(index, filename)
    print('Saving index', filename, 'with', index.ntotal, 'items...')


def loadIndex(filename):
    if os.path.exists(filename):
        f = open(filename, 'rb')

        reader = faiss.PyCallbackIOReader(f.read, 1234)
        reader = faiss.BufferedIOReader(reader, 1234)

        index = faiss.read_index(reader)
        print('Index', filename, 'loaded', index.ntotal, 'items')
        return index
    else:
        print('Index', filename, 'not found')
        return None


def createIndex(model_size):
    print('Creating index...', end='')
    #nlist = 6  # Voronoi cells partition
    #quantizer = faiss.IndexFlatIP(model_size)
    #index = faiss.IndexIVFFlat(quantizer, model_size, nlist)
    index = faiss.IndexFlatIP(model_size)
    index = faiss.IndexIDMap(index)
    print('ok')
    return index


def cleanHeaders(table):
    headers = list(table.columns.values)
    headers = [str(head).lower().replace("_", " ").replace("-", " ") for head in headers]
    return headers


def cleanContent(table):
    clean_content = []
    content = list(table.columns.values)
    for col in content:
        col_content = list(table[col].values)
        col_content = list(dict.fromkeys(col_content))  # Remove duplicates
        col_content = [str(col).lower().replace("_", " ").replace("-", " ") for col in col_content]
        col_content = ' '.join(col_content)
        clean_content.append(col_content)

    return clean_content


def initOpenSearch():
    HOST = os.getenv('OPENSEARCH_HOST')
    print(HOST)
    client = OpenSearch(
        hosts=[{'host': HOST, 'port': 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    if not client.indices.exists(OPENSEARCH_INDEX):
        client.indices.delete(index=OPENSEARCH_INDEX)

        f = open(os.path.dirname(__file__)+'/schema.json')
        body = json.load(f)
        client.indices.create(OPENSEARCH_INDEX, body=body[0])
        f.close()

    return client
