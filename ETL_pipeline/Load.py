import pyarrow.parquet as pq
import os
import psycopg2
from dotenv import load_dotenv
import io

load_dotenv()

def write_to_parquet(data):
    # PyArrow 테이블을 Parquet 파일로 저장
    pq.write_table(data, 'data/cleaned_data.parquet')

def load_to_db(data_path):
    # PostgreSQL 연결
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()

    # Parquet 파일 읽기
    table = pq.read_table(data_path)
    df = table.to_pandas()

    # CSV buffer 생성
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    # 데이터베이스에 데이터 삽입
    cursor.copy_from(buffer, "aol_data", sep=",", columns=tuple(df.columns))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded to database successfully.")

