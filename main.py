from ETL_pipeline.Extract import extract
import modin.pandas as pd

if __name__ == "__main__":
    data = extract()
    print(data.__next__())