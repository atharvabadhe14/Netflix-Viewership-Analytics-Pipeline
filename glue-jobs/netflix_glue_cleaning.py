from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, regexp_extract, to_date, year

spark = SparkSession.builder.getOrCreate()

INPUT_PATH = "s3://netflix-etl-data-bucket/raw/"
OUTPUT_PATH = "s3://netflix-etl-data-bucket/processed/netflix_cleaned/"

df = spark.read.option("header", "true").csv(INPUT_PATH)

# Trim all string columns
for c in df.columns:
    df = df.withColumn(c, trim(col(c)))

# Convert date_added to date
df = df.withColumn("date_added", to_date(col("date_added"), "MMMM d, yyyy"))

# Remove invalid countries
df = df.filter(
    (col("country").isNotNull()) &
    (col("country") != "Not Given")
)

# Drop director column
df = df.drop("director")

# Standardize duration
df = df.withColumn(
    "duration_value",
    regexp_extract(col("duration"), "(\\d+)", 1)
)

# Feature engineering
df = df.withColumn("year_added", year(col("date_added")))

# Remove duplicates
df = df.dropDuplicates()

# Write cleaned data
df.write.mode("overwrite").parquet(OUTPUT_PATH)
