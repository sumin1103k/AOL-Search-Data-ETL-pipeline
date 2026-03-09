import pyarrow.parquet as pq
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def write_to_parquet(data):
    # PyArrow 테이블을 Parquet 파일로 저장
    pq.write_table(data, 'data/cleaned_data.parquet')

#def load_to_db()
