from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from opensearchpy import OpenSearch, RequestsHttpConnection
import configparser
import uvicorn
import requests
from lingua import Language, LanguageDetectorBuilder


config = configparser.ConfigParser()
config.read("./config.ini")

host = 'search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com'
region = 'eu-west-3'

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

languages = [Language.ENGLISH, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/details/")
async def search(id):
    resp = client.search(index="search-test", body={"query":{"terms": {"_id": [id]}}})

    result = resp['hits']['hits'][0]['_source']

    return {"results": result}


@app.post("/search-table/")
async def searchTable(data: Request):

    url = 'http://localhost:5000/search'
    x = requests.post(url, json = await data.json())
    return x.json()


@app.get("/search/")
async def search(keywords:str):
    lang = detector.detect_language_of(keywords)
    query_lang = 'es'

    if lang == Language.ENGLISH:
        query_lang = 'en'

    resp = client.search(index="search-test", size=1000, body={"query":{
        "match": {
            "title_"+query_lang: {
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000, reload=True)
