from datetime import datetime
import pandas as pd
import os
import json
import random
from tqdm import tqdm
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

# Successful response!
print(client.info())
response = client.indices.delete(
    index = 'search-v1'
)

files = os.listdir("./data/datos.gob.es") # all files in data
for file in tqdm(files):
    if file[:5]== 'meta_':
        try:
            with open("./data/datos.gob.es/" + file, 'r') as f:
                data = json.load(f)
                
            doc = {
                'title': data['title'],
                'description': data['description'],
                'theme': data['theme'],
                'modified': data['modified'],
                'license' : data['license'],
                'provider': 'Datos.gob.es',
                'resources': data['resources']
            }

            resp = client.index(index="search-v1", id=random.randint(0,9999999), body=doc, refresh=True)
        except Exception:
            pass