import subprocess
import requests
import json
import os
from opensearchpy import OpenSearch, RequestsHttpConnection
from dotenv import load_dotenv

load_dotenv('.env')

ENVIRONMENT = os.getenv('ENVIRONMENT')

# OpenSearch Config
OPENSEARCH_INDEX = os.getenv('OPENSEARCH_INDEX')
USERNAME = os.getenv('OPENSEARCH_USERNAME')
PASS = os.getenv('OPENSEARCH_PASS')
auth = (USERNAME, PASS)

# Embeddings Config
HOST_EMB = os.getenv('HOST_EMB')


def downloadMeta(domain):
    save_path = os.path.join(os.path.dirname(__file__), 'data/')

    python_path = '/usr/local/bin/python'
    if ENVIRONMENT == 'test':
        python_path = 'python'

    with subprocess.Popen([python_path,
                           '-m',
                           'opendatacrawler',
                           '-d', domain, '-m', '-t',
                           'csv', '-nd', '-p', save_path]) as proc:
        while proc.poll() is None:
            pass


def downloadMetaAndData(domain, id):
    save_path = os.path.join(os.path.dirname(__file__), 'tmp/')
    python_path = '/usr/local/bin/python'
    if ENVIRONMENT == 'test':
        python_path = 'python'
    with subprocess.Popen([python_path,
                           '-m',
                           'opendatacrawler',
                           '-d', domain, '-pd', '-t','csv','-m',
                           '-id', id, '-p', save_path],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT
                            ) as proc:
        while proc.poll() is None:
            pass


def translate(text, lng):
    data = {
        "input_text": text,
        "target_lang": lng
    }
    response = requests.post('http://'+HOST_EMB+':8000/translate/', json=data)
    if response.status_code == 200:
        return response.json()['response']
    else:
        return None


def clean_url(u):
    """Clean a url string to obtain the mainly domain without protocols."""

    if u.startswith("http://"):
        u = u[7:]
    if u.startswith("https://"):
        u = u[8:]
    if u.startswith("www."):
        u = u[4:]
    if u.endswith("/"):
        u = u[:-1]
    return u.split('/')[0]


def indexFaiss(table, id):
    response = requests.post('http://'+HOST_EMB+':5000/index/', json={'data': table,'id': id})
    if response.status_code == 200:
        return response.json()


def saveIndexFaiss():
    response = requests.get('http://'+HOST_EMB+':5000/saveIndexes/')
    if response.status_code == 200:
        return response.json()


def initOpenSearch():
    HOST = os.getenv('OPENSEARCH_HOST')

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


def indexRedis(r, resource_id, data):
    r.set(resource_id, data)


def indexOpenSearch(client, meta, df, portal):
    df.reset_index(inplace=True, drop=True)
    if len(df.index) > 20:
        df = df.sample(n=20)
    sample = df.to_json(orient="split")

    title_trans = translate(meta['title'], 'en')
    desc_trans = translate(meta['description'], 'en')

    doc = {
        "identifier": meta['id_portal'],
        "title_en": title_trans,
        "title_es": meta['title'],
        "title": meta['title'],
        "img_portal": portal['img'],
        "description": meta['description'],
        "description_en": desc_trans,
        "description_es": meta['description'],
        "language": portal['language'],
        "theme": meta['theme'],
        "resources": meta['resources'],
        "issued": meta.get('issued', None),
        "modified": meta.get('modified', None),
        "license": meta.get('license', None),
        "provider": portal['url'],
        "temporal": meta.get('temporal', None),
        "spatial_coverage": portal['spatial_coverage'],
        "sample": sample
    }
    client.index(id=meta['id_custom'], index=OPENSEARCH_INDEX, body=doc, refresh=True)


def updateIndexOpenSearch(client, meta, portal):

    title_trans = translate(meta['title'], 'en')
    desc_trans = translate(meta['description'], 'en')

    doc = {
        "identifier": meta['id_portal'],
        "title_en": title_trans,
        "title_es": meta['title'],
        "img_portal": portal['img'],
        "description_en": desc_trans,
        "description_es": meta['description'],
        "language": portal['language'],
        "theme": meta['theme'],
        "resources": meta['resources'],
        "issued": meta.get('issued', None),
        "modified": meta.get('modified', None),
        "license": meta.get('license', None),
        "provider": portal['url'],
        "temporal": meta.get('temporal', None),
        "spatial_coverage": portal['spatial_coverage']
    }
    client.index(id=meta['id_custom'], index=OPENSEARCH_INDEX, body=doc, refresh=True)
