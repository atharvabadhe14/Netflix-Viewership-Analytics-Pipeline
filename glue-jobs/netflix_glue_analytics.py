from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, explode, split

spark = SparkSession.builder.getOrCreate()

INPUT_PATH = "s3://netflix-etl-data-bucket/processed/netflix_cleaned/"
OUTPUT_BASE = "s3://netflix-etl-data-bucket/curated/"

df = spark.read.parquet(INPUT_PATH)

# Content type summary
df.groupBy("type") \
  .agg(count("*").alias("count")) \
  .write.mode("overwrite") \
  .parquet(OUTPUT_BASE + "content_type_summary/")

# Country-wise distribution
df.groupBy("country", "type") \
  .agg(count("*").alias("count")) \
  .write.mode("overwrite") \
  .parquet(OUTPUT_BASE + "content_by_country/")

# Rating distribution
df.groupBy("rating", "type") \
  .agg(count("*").alias("count")) \
  .write.mode("overwrite") \
  .parquet(OUTPUT_BASE + "rating_distribution/")

# Yearly trend
df.groupBy("year_added", "type") \
  .agg(count("*").alias("count")) \
  .orderBy("year_added") \
  .write.mode("overwrite") \
  .parquet(OUTPUT_BASE + "yearly_content_trend/")

# Genre distribution
df.withColumn("genre", explode(split(col("listed_in"), ", "))) \
  .groupBy("genre") \
  .agg(count("*").alias("count")) \
  .write.mode("overwrite") \
  .parquet(OUTPUT_BASE + "genre_distribution/")
