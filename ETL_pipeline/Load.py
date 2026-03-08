import modin.pandas as pd

def load(data):
    # 데이터 저장 (예: CSV 파일로 저장)
    data.to_csv("cleaned_data.csv", index=False)