import pandas as pd
import os
import json
import random
from tqdm import tqdm
from opensearchpy import OpenSearch, RequestsHttpConnection
import configparser
import csv

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

files = os.listdir("/home/alberto/OpenDataCrawler/data/datos.gob.es") # all files in data
for file in tqdm(files):
    if file[:5]== 'meta_':
        try:
           
            with open("/home/alberto/OpenDataCrawler/data/datos.gob.es" + file, 'r') as f:
                data = json.load(f)
                for re in data['resources']:
                    if re['path'] is not None:
                        if re['path'][-3:]=='csv':
                            sample = pd.read_csv(re['path'], encoding = "ISO-8859-1", on_bad_lines='skip', engine='python', sep = None )
                            sample.reset_index(inplace=True, drop=True)
                            sample = sample.to_json(orient="split")
                        else:
                            sample = None
                        break

                doc = {
                    'title': data['title'],
                    'img': data['img'],
                    'description': data['description'],
                    'theme': data['theme'],
                    'issued': data['issued'],
                    'modified': data['modified'],
                    'license' : data['license'],
                    'provider': data['source'],
                    'resources': data['resources'],
                    'temporal': data['temporal'],
                    'geo': data['geo'],
                    'sample': sample
                }

                resp = client.index(index="search-v1", id=random.randint(0,9999999), body=doc, refresh=True)
        except Exception as e:
            print(e)
            pass