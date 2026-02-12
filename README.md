# Netflix Viewership Analytics Pipeline

An end-to-end, event-driven AWS ETL pipeline to ingest, transform, analyze, and visualize Netflix viewership data at scale using serverless cloud services.

---

## 📌 Project Overview

This project demonstrates a production-style data engineering pipeline built on AWS. Raw Netflix viewership data is automatically ingested, cleaned, transformed into analytics-ready datasets, queried using SQL, and visualized through interactive dashboards.

The architecture follows industry best practices with clear separation between ingestion, processing, analytics, and visualization layers.

---

## 🏗️ Architecture Overview

**End-to-End Flow:**

1. Raw Netflix data is uploaded to Amazon S3 (`raw/` zone)
2. An S3 event triggers an AWS Lambda function
3. Lambda starts an AWS Glue Workflow
4. Glue Job 1 cleans and standardizes raw data
5. Glue Job 2 performs aggregations and analytics using PySpark
6. Curated Parquet datasets are stored in S3
7. Amazon Athena provides a SQL interface over curated data
8. Tableau consumes Athena tables for visualization

---

## 🧰 Tech Stack

- **Cloud Platform:** AWS  
- **Storage:** Amazon S3  
- **Orchestration:** AWS Lambda, AWS Glue Workflow  
- **Processing:** AWS Glue (PySpark)  
- **Query Engine:** Amazon Athena (SQL)  
- **Visualization:** Tableau  
- **Data Format:** Parquet  
- **Languages:** Python, SQL  

---

## 📂 Project Structure

```
Netflix-Viewership-Analytics-Pipeline/
├── glue-jobs/
│   ├── netflix_glue_cleaning.py
│   └── netflix_glue_analytics.py
├── lambda/
│   └── trigger_glue_workflow.py
├── athena/
│   ├── create_database.sql
│   ├── create_tables.sql
│   └── sample_queries.sql
├── diagrams/
│   └── architecture.txt
└── README.md
```

---

## 🔄 Data Zones (S3)

- **Raw Zone:** `s3://netflix-etl-data-bucket/raw/`
- **Processed Zone:** `s3://netflix-etl-data-bucket/processed/`
- **Curated Zone:** `s3://netflix-etl-data-bucket/curated/`
- **Athena Results:** `s3://netflix-etl-data-bucket/athena-results/`

---

## 📊 Analytics Generated

- Genre distribution
- Content type summary (Movies vs TV Shows)
- Country-wise content availability
- Rating distribution
- Year-wise content trends

---

## 💡 Key Highlights

- Event-driven and fully automated pipeline
- Serverless architecture for scalability and cost efficiency
- Columnar storage (Parquet) for optimized analytics
- SQL-based analytics without data movement
- BI-ready datasets consumed by Tableau

---

## 🧠 Interview Explanation (Short)

> Raw data uploaded to S3 triggers a Lambda function that starts a Glue workflow. Glue jobs clean and aggregate the data using PySpark and store curated Parquet datasets in S3. Athena provides a serverless SQL layer over this data, which is finally visualized using Tableau dashboards.

---

## 📎 Notes

- AWS resources (S3 buckets, IAM roles, Glue workflows) are not stored in GitHub.
- This repository contains the code and architecture logic used in the pipeline.
