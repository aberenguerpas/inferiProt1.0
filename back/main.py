from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from opensearchpy import OpenSearch, RequestsHttpConnection

host = 'search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com'
region= 'eu-west-3'
auth = ('Elastiko', '#In_ferI4')

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

    resp = client.search(index="search-test", size=1000, body={"query":{"match": {"title": {"query": keywords}}}})

    result = []
    total = resp['hits']['total']['value']

    for hit in resp['hits']['hits']:
        data = hit['_source']

        result.append(data)

    return {"results": result, "total": total}