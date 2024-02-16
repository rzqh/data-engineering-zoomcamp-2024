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

    # Membagi data dalam chunk (chunking)
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Mendapatkan chunk pertama dan menyimpannya ke dalam variabel df
    df=next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    # Memasukkan data ke database
    ## Memasukkan header untuk membentuk tablenya
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    
    ## Selanjutnya akan memasukkan datanya
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Looping sampai terjadi exception (seperti stopiteration)
    while True:
        try:
            t_start = time() # menandai waktu mulai proses

            df = next(df_iter) # mengambil chunk berikutnya dari iterator df_iter

            # mengubah kolom tpep_pickup_datetime dan tpep_dropoff_datetime
            # dari format string ke datetime menggunakan pandas.to_datetime
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            # menyimpan DataFrame ke dalam tabel SQL 'yellow_taxi_data',
            # - 'con=engine' menggunakan engine SQLAlchemy yang telah dibuat sebelumnya untuk koneksi database
            # - 'if_exists=append' berarti bahwa data akan ditambahkan ke tabel jika tabel itu sudah ada
            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time() # Menandai waktu akhir proses

            # Mencetak waktu yang diperlukan untuk proses dan pemasukan chunk data tersebut
            print('inserted another chunk, took %.3f second' % (t_end - t_start))
            
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


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