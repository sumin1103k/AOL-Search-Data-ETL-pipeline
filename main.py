from ETL_pipeline.Extract import extract
from ETL_pipeline.Transform import transform
from ETL_pipeline.Transform import clean
from ETL_pipeline.Load import write_to_parquet


if __name__ == "__main__":
    data = extract()
    trans_data = transform(data)
    clean_data = clean(trans_data)
    write_to_parquet(clean_data)