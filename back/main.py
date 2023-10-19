from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from opensearchpy import OpenSearch, RequestsHttpConnection
from lingua import Language, LanguageDetectorBuilder
from dotenv import load_dotenv
from google.cloud import dialogflow
import configparser
import uvicorn
import requests
import os
import requests
import time


def llm_callback(text):
    r = requests.post(
        'http://localhost:6000/fallback',
        json={'data': text},
        headers={
            "Content-Type": "application/json"
        }
    )
    return r.json()['msj']


def detect_intent_texts(project_id, session_id, texts, language_code):

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        return response.query_result


load_dotenv()  # take environment variables from .env.
config = configparser.ConfigParser()
config.read("./config.ini")

host = 'search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com'
username = config['credentials']['username']
password = config['credentials']['password']
auth = (username, password)

# Create the client with SSL/TLS and hostname verification disabled.
client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
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


@app.get("/tags/")
async def tags(tags:str):   
    tags = ['{"term":{"title":"'+t+'"}}' for t in tags.split(",")]
    body = """{
        "query":{
                    "bool": {
                    "should": ["""+ ",".join(tags) + """]
                    }
                }
        }"""
    resp = client.search(index="search-v1", size=200, body=body)
    result = []
    total = resp['hits']['total']['value']

    for hit in resp['hits']['hits']:
        data = hit['_source']
        data['id'] = hit['_id']

        result.append(data)

    return {"results": result, "total": total}


@app.get("/details/")
async def search(id):
    resp = client.search(index="search-test", body={"query":{"terms": {"_id": [id]}}})

    result = resp['hits']['hits'][0]['_source']

    return {"results": result}


@app.post("/search-table/")
async def searchTable(data: Request):

    url = 'http://localhost:5000/search'
    x = requests.post(url, json=await data.json())
    return x.json()


@app.get("/search/")
async def search(keywords:str, geo:str=None, license:str=None, price:float=None, provider:str=None, last_update:str=None, first:bool=None):
    lang = detector.detect_language_of(keywords)
    query_lang = 'es'

    if lang == Language.ENGLISH:
        query_lang = 'en'

    query = {
        "query": {
            "bool": {
                "must": [{
                        "match": {
                            "title_"+query_lang: {
                                "query": keywords,
                                "fuzziness": "auto"
                            }
                        }
                    }]
            }

        }
    }

    if geo:
        query['query']['bool']['must'].append({
                        "match": {
                            "spatial_coverage": {
                                "query": geo
                            }
                        }
                    })

    if license:
        query['query']['bool']['must'].append({
                        "term": {
                            "license.keyword": license,
                        }
                    })
    if provider:
        query['query']['bool']['must'].append({
                        "term": {
                            "provider.keyword": provider
                        }
                    })
    if last_update:
        query['query']['bool']['must'].append({
                        "range": {
                            "issued": {"gte": last_update}
                        }
                    })
    if price:
        if price > 0:
            query['query']['bool']['must'].append({
                            "range": {
                                "price": {"gt": 0}
                            }
                        })
        else:
            query['query']['bool']['must'].append({
                            "range": {
                                "price": {"lte": 0}
                            }
                        })

    # Primera vez que hace la búsqueda devuelve los filtros
    if first:
        filters = {'aggs': {
           "providers": {
                "terms": {
                    "field": "provider.keyword"
                }
            },
           "geo": {
                "terms": {
                    "field": "spatial_coverage.keyword"
                }
            },
                "license": {
                "terms": {
                    "field": "license.keyword"
                }
            }
        }
    }
        
    query2 = query | filters

    resp = client.search(index="search-v1", size=1000, body=query)
    result = []
    total = resp['hits']['total']['value']

    for hit in resp['hits']['hits']:
        data = hit['_source']
        data['id'] = hit['_id']

        result.append(data)

    return {"results": result, "total": total}


@app.post("/send_chat_form/")
async def send_hubspot_form(d: Request):

    form = await d.json()
    portal_id = '26607839'
    form_id = 'ea5863d6-ba85-4ee8-a94b-efc0a41baeac'
    url = 'https://api.hsforms.com/submissions/v3/integration/secure/submit/'+portal_id+'/'+form_id

    data = {
            "submittedAt": int(time.time()*1000),
            "fields": [
                {
                    "name": "firstname",
                    "value": form['name'],
                    "objectTypeId": "0-1"
                },
                {
                    "name": "email",
                    "value": form['email'],
                    "objectTypeId": "0-1"
                },
                {
                    "name": "datos_que_puede_aportar",
                    "value": form['data'],
                    "objectTypeId": "0-1"
                },
                {
                    "name": "formato_interes",
                    "value": form['format'],
                    "objectTypeId": "0-1"
                },
                {
                    "name": "necesidad_temporal",
                    "value": "Otro",
                    "objectTypeId": "0-1"
                },
                {
                    "name": "lifecyclestage",
                    "value": "lead",
                    "objectTypeId": "0-1"
                },
                {
                    "name": "lifecyclestage",
                    "value": "lead",
                    "objectTypeId": "0-2"
                }
            ],
            "pageUrl": "https://www.inferia.io/solicitar_datos/"
    }
    r = requests.post(
        url,
        json=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer "+ os.getenv('API_HUBSPOT')}
    )

    if r.status_code == 200:
        return r.json()
    else:
        return {'status': 'Error ' + str(r.status_code), 'data': r.json()}


@app.post("/chatbot/")
async def chatbot(data: Request):
    text = await data.json()
    print(text)
    response =  detect_intent_texts(os.environ["DF_PROJECT_ID"], text['chat_id'], [text['data']], 'es-ES')

    if response.intent.display_name == 'Default Fallback Intent':

        llm_res = llm_callback(response.query_text)
        return {'msj': llm_res, 'type': 'json', 'intent': response.intent.display_name}

    if response.fulfillment_text[0]!='{':
        type = "text"
    else:
        type = "json"

    return {'msj': response.fulfillment_text, 'type': type, 'intent': response.intent.display_name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000, reload=True)
