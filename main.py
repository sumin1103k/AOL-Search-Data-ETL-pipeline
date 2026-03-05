import ETL_pipeline.Extract as Extract

# 샘플 크기를 조정하여 로드 시간 단축 (예: 100, 1000, 10000)
sample_size = 100  # 필요에 따라 변경
df = Extract.Extract(sample_size)
print(f"Loaded {len(df)} records")
print(df.head())