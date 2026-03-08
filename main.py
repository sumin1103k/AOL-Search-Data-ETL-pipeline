from ETL_pipeline.Extract import extract
from ETL_pipeline.Transform import transform
from ETL_pipeline.Transform import clean
from ETL_pipeline.Load import load


if __name__ == "__main__":
    data = extract()
    #print(data.__next__())
    trans_data = transform(data)
    clean_data = clean(trans_data)
    load(clean_data)