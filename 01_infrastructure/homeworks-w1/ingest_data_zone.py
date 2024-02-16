#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import argparse
from sqlalchemy import create_engine
from time import time # import modul time untuk tracking waktu
import os 

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    url = params.url
    table_name = params.table_name
    
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'
        
    # download dan rename dataset
    os.system(f"wget {url} -O {csv_name}")  
    
    # format URL: 'postgresql"//[user]:[password]@[host]:[port]/[dbname]'
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    
    # membaca dataset
    df = pd.read_csv(csv_name)
    # Memasukkan data ke database
    df.to_sql(name=table_name, con=engine, if_exists='append')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument('--user', required=True, help='username for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for posgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--dbname', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='table name for postgres')
    parser.add_argument('--url', required=True, help='raw data url')
    

    args = parser.parse_args()
    
    main(args)