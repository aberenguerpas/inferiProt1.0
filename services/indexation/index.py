import os
import glob
import json
import redis
import pandas as pd
from tqdm import tqdm
from utils import *
from dotenv import load_dotenv

load_dotenv('.env')

# CONSTANTS
DATA_PATH = os.getenv('DATA_PATH')
HOST_REDIS = os.getenv('HOST_REDIS')
PORTALS_PATH = os.getenv('PORTALS_PATH')
print(HOST_REDIS)

def main():
    #  Read portals list
    f = open(os.path.dirname(__file__)+ PORTALS_PATH)
    portals = json.load(f)

    # Load redis database 0
    r = redis.Redis(host=HOST_REDIS, port=6379, db=0) # Database dataset update time
    
    r.flushdb() # remove redis db

    # Init OpenSearch client
    open_client = initOpenSearch()

    for portal in portals:
        # Download all portal metadata
        downloadMeta(portal['portal'])

        portal_name = clean_url(portal['portal'])
        meta_path = os.path.join(os.path.join(os.path.dirname(__file__), DATA_PATH), portal_name)

        files = os.listdir(meta_path)
        files = [x for x in files if x.startswith("meta_")]  # Get meta info files

        # Check all metadata files and Cheking are already indexed
        for file in tqdm(files):
            try:
                # Load metadata file
                f = open(os.path.join(meta_path, file))
                meta = json.load(f)
                resource_id = meta['id_custom']

                # Exist in redis database?
                exist_data = r.exists(resource_id)
                data_modified = meta['modified']
                if exist_data:
                    # Are the data updated?
                    if r.get(resource_id).decode("utf-8") == data_modified:
                        print('Resource already update')  # Finish
                    else:
                        print('Resource needs to be update')

                        # Update resource
                        downloadMetaAndData(portal['portal'], meta['id_portal'])
                        updateIndexOpenSearch(open_client, meta, portal)
                        indexRedis(r, resource_id, data_modified)

                else:
                    print('No exist resource', resource_id, 'Creating...')

                    # Create and index resource
                    downloadMetaAndData(portal['portal'], meta['id_portal'])
                    p1 = os.path.dirname(__file__)
                    result_files = glob.glob(p1+'/tmp/'+portal_name+'/meta_'+resource_id + "**") 
                    print(result_files)
                    f = open(result_files[0])
                    meta = json.load(f)
                    for resource in meta['resources']:
                        # The resource with path are indexed
                        if 'path' in resource and resource['path'] is not None:
                            df = None

                            # list of encodings to try
                            encodings = ['utf8', 'latin1', 'cp1252']
                            for enco in encodings:
                                try:
                                    df = pd.read_csv(
                                                    resource['path'],
                                                    on_bad_lines='skip',
                                                    engine='python',
                                                    sep=None,
                                                    encoding=enco)
                                except Exception as e:
                                    print(e)
                                    continue
                            if df is not None:

                                df_json = df.to_json(orient="split")
                                print(resource_id)
                                indexFaiss(df_json, resource_id)
                                indexRedis(r, resource_id, data_modified)
                                indexOpenSearch(open_client, meta, df, portal)

                                break
                        # print('Resource not created, path not available')
                    # Remove tmeporal files
                    for f in os.listdir(p1+'/tmp/' + portal_name):
                        os.remove(os.path.join(p1+'/tmp/' + portal_name, f))
            except Exception as e:
                print(e)

        saveIndexFaiss()


if __name__ == "__main__":
    main()
