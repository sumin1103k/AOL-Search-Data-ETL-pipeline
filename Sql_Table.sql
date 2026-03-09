CREATE TABLE aol_data(
  num BIGSERIAL PRIMARY KEY,
  user_id INT,
  query_id TEXT NOT NULL,
  query TEXT NOT NULL,
  query_orig TEXT NOT NULL,
  time TIMESTAMP NOT NULL,
  rank INT,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE (user_id, query, time, rank)
);

CREATE INDEX idx_aol_data_user
ON aol_data(user_id);

CREATE INDEX idx_aol_data_query
ON aol_data(query);

CREATE INDEX idx_aol_data_query_orig
ON aol_data(query_orig);

CREATE INDEX idx_aol_data_time
ON aol_data(time);

CREATE INDEX idx_aol_data_query_time
ON aol_data(query, time);

CREATE INDEX idx_aol_data_query_rank
ON aol_data(query, rank);