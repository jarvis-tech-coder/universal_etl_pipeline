Universal ETL Data Pipeline (v1-core)

A production-style ETL (Extract–Transform–Load) pipeline built with Python that automatically ingests data from multiple sources, processes it, loads it into PostgreSQL, and generates analytical reports — all orchestrated via a single runner.

Project Overview

This project demonstrates how a real-world data engineering ETL pipeline works end-to-end:
    Incoming Data → Extract → Transform → Load → Report

Key highlights:

Fully automated execution
Clean folder & package structure
Database-backed (PostgreSQL)
Logging & fault tolerance
Resume & interview ready

Data Flow

1.Incoming files are placed in data/incoming/

2.Runner detects new files

3.Data is:
 
    Extracted (CSV / JSON / API)

    Transformed (cleaning, calculations)

    Loaded into PostgreSQL

4.Files are archived to data/processed/

5.Final Excel report is generated

Tech Stack

    Python
    PostgreSQL
    pandas
    psycopg2
    pgAdmin

Setup Instructions

1.Clone Repository

git clone <your-repo-url>
cd v1-core

2.Create & Activate Virtual Environment (Windows)

python -m venv venv
venv\Scripts\activate.bat

3.Install Dependencies

pip install pandas psycopg2-binary requests openpyxl

4.PostgreSQL Setup
    Create database: etl_db
    Create table:

    CREATE TABLE sales (
    order_id INT,
    order_date DATE,
    product VARCHAR(100),
    quantity INT,
    price NUMERIC,
    total_amount NUMERIC,
    customer_id INT
);


Run the Pipeline
From project root (v1-core):

set PYTHONPATH=.
python -m etl_scripts.runner


Supported Input Formats

    CSV files
    JSON files
    API-based data (extensible)

Future Enhancements (v2)

    SQLAlchemy integration
    Schema auto-creation
    Airflow / Cron scheduling
    Dockerization
    Incremental & CDC loads
    Data quality checks


Author

Asad
Data Engineering Enthusiast
    GitHub: (add link)
    LinkedIn: (add link)