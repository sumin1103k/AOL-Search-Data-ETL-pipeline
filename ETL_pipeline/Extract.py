import ir_datasets

def extract():

    # 데이터셋 로드
    dataset = ir_datasets.load("aol-ia")

    # 퀴리 로그 데이터 추출
    data = dataset.qlogs_iter()
    
    return data