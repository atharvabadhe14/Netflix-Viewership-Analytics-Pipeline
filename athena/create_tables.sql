CREATE EXTERNAL TABLE netflix_analytics.genre_distribution (
  genre STRING,
  count BIGINT
)
STORED AS PARQUET
LOCATION 's3://netflix-etl-data-bucket/curated/genre_distribution/';
