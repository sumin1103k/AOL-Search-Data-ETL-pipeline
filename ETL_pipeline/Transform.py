import pyarrow as pa
import modin.pandas as pd

def transform(data, yield_chunk_size = 100_000) -> pa.Table:

    rows = []

    # 쿼리 로그 데이터를 PyArrow 테이블로 변환
    for q in data:

        # 쿼리 로그의 클릭 문서가 없거나 검색어가 없을 경우 제외
        if q.items is None or q.query_id == "d41d8cd98f00b2":
            continue
        else:
            for item in q.items:
                rows.append({
                    "user_id": q.user_id,
                    "query_id": q.query_id,
                    "query": q.query,
                    "query_orig": q.query_orig,
                    "time": q.time,
                    "rank": item.rank,
                })

                if len(rows) >= yield_chunk_size:
                    yield pa.Table.from_pylist(rows)
                    rows.clear()

    if rows:
        yield pa.Table.from_pylist(rows)


def clean(data: pa.Table) -> pd.DataFrame:
    data = next(data)

    # PyArrow 테이블을 Pandas DataFrame으로 변환
    df = data.to_pandas()
    # 데이터 결측치 제거
    df = df.dropna()
    # 데이터 중복 제거
    df = df.drop_duplicates()
    # 데이터 타입 변환
    df['user_id'] = df['user_id'].astype(int)
    df['query_id'] = df['query_id'].astype(str)
    df['query'] = df['query'].astype(str)
    df['query_orig'] = df['query_orig'].astype(str)
    df['time'] = pd.to_datetime(df['time'])
    df['rank'] = df['rank'].astype(int)
    # 다시 PyArrow 테이블로 변환
    clean_table = pa.Table.from_pandas(df)
    
    return clean_table