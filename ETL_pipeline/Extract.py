import ir_datasets
import modin.pandas as pd
from itertools import islice

def Extract(sample_size=100):
    # 데이터 로드
    dataset = ir_datasets.load("aol-ia")
    
    # 쿼리 로그 데이터프레임으로 변환 (샘플 크기 제한)
    # AolQlog 객체를 dict로 변환하여 DataFrame 생성
    data = [item._asdict() for item in islice(dataset.qlogs_iter(), sample_size)]
    df = pd.DataFrame(data)
    return df