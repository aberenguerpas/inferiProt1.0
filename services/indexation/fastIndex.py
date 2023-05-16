import os
import glob
import json
import pandas as pd
from tqdm import tqdm
from utils import *
from dotenv import load_dotenv

load_dotenv('.env')

# CONSTANTES
DATA_PATH = os.getenv('DATA_PATH')
PORTALS_PATH = os.getenv('PORTALS_PATH')

def main():
    #  Read portals list
    f = open(os.path.dirname(__file__)+ PORTALS_PATH)
    portals = json.load(f)

    # Init OpenSearch client
    open_client = initOpenSearch()

    for portal in portals:
        print('Indexing portal', portal)

        portal_name = clean_url(portal['portal'])
        meta_path = os.path.join(os.path.join(os.path.dirname(__file__), DATA_PATH), portal_name)
        #meta_path = os.path.join('/Users/albertoberenguerpastor/Desktop/InferIA/inferiProt1.0/data/data', portal_name)
        files = os.listdir(meta_path)
        files = [x for x in files if x.startswith("meta_")]  # Get meta info files

        # Check all metadata files and Cheking are already indexed
        for file in tqdm(files):
            try:
                # Load metadata file
                f = open(os.path.join(meta_path, file))
                meta = json.load(f)
                resource_id = meta['id_custom']
                for resource in meta['resources']:
                    # The resource with path are indexed
                    if 'path' in resource and resource['path'] is not None:
                        df = None
                        
                        # list of encodings to try
                        encodings = ['utf8', 'latin1', 'cp1252']
                        for enco in encodings:
                            try:
                                df = pd.read_csv(
                                                "/".join(resource['path'].split("/")[-3:]),
                                                on_bad_lines='skip',
                                                engine='python',
                                                sep=None,
                                                encoding=enco)
                                break
                            except Exception as e:
                                print(e)
                                continue
                        if df is not None:

                            df_json = df.to_json(orient="split")
                            print(resource_id)
                            indexFaiss(df_json, resource_id)
                            indexOpenSearch(open_client, meta, df, portal)
                            break
            except Exception as e:
                print(e)

        saveIndexFaiss()


if __name__ == "__main__":
    main()