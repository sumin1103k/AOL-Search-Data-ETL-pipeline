import ir_datasets
import modin.pandas as pd


def extract(yield_chunk_size=100_000):

    # Load the raw dataset
    dataset = ir_datasets.load("aol-ia")
    iterable = dataset.qlogs_iter()
    rows = []

    # Convert the iterable of query logs into a DataFrame in chunks
    for q in iterable:
        rows.append({
            'user_id': q.user_id,
            'query_id': q.query_id,
            'query': q.query,
            'query_orig': q.query_orig,
            'time': q.time,
        })

        if len(rows) >= yield_chunk_size:
            yield pd.DataFrame(rows)
            rows.clear()

    if rows:
        yield pd.DataFrame(rows)