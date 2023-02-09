from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from opensearchpy import OpenSearch, RequestsHttpConnection
import configparser

config = configparser.ConfigParser()
config.read("./config.ini")

host = 'search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com'
region= 'eu-west-3'

username = config['credentials']['username']
password = config['credentials']['password']
auth = (username, password)

# Create the client with SSL/TLS and hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
async def search(keywords:str):

    resp = client.search(index="search-test", size=1000, body={"query":{
        "match": {
            "title": {
                "query": keywords,
                "fuzziness": "auto"
                }
            }
        }
    })

    result = []
    total = resp['hits']['total']['value']

    for hit in resp['hits']['hits']:
        data = hit['_source']
        data['id'] = hit['_id']

        result.append(data)

    return {"results": result, "total": total}

@app.get("/details")
async def search(id):

    resp = client.search(index="search-v1", body={"query":{"terms": {"_id": [id]}}})

    result = resp['hits']['hits'][0]['_source']

    return {"results": result}

@app.get("/search-test")
async def searchTest(keywords:str):
    resp = client.search(index="search-v1", size=1000, body={"query":{"match": {"title": {"query": keywords}}}})

    result = []
    total = resp['hits']['total']['value']

    for hit in resp['hits']['hits']:
        data = hit['_source']
        data['id'] = hit['_id']

        result.append(data)

    return {"results": result, "total": total}