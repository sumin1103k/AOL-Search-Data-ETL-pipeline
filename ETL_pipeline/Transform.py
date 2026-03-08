import modin.pandas as pd

def transform(data, yield_chunk_size = 100_000):

    rows = []

    # 쿼리 로그 데이터를 PyArrow 테이블로 변환
    for q in data:

        # 쿼리 로그의 클릭 문서가 없을 경우 제외
        if q.items is None:
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
                    yield pd.DataFrame(rows)
                    rows.clear()

    if rows:
        yield pd.DataFrame(rows)


def clean(data):
    df = data.__next__()
    # 데이터 결측치 제거
    df = df.dropna()
    # 데이터 중복 제거
    df = df.drop_duplicates()
    
    return df