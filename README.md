# Australia Weather Pipeline: End-to-End Medallion Architecture
**Hema Siddartha Reddy Yalluri** | *Data Engineer*

## Project Overview
This project implements a production-grade data pipeline that ingests raw Australian weather data from **Google Cloud Storage (GCS)**, processes it through a **Medallion Architecture (Bronze, Silver, Gold)** using **Apache Spark**, and automates the entire flow using **Apache Airflow**.

The primary objective was to build a robust, self-healing system that prioritizes **data quality**, **security**, and **scalability**.

---

##  Architecture
The pipeline follows a modern cloud-data stack pattern, decoupling storage from compute and utilizing a centralized orchestrator.

### **Tech Stack**
* **Cloud Provider:** Google Cloud Platform (GCP)
* **Storage:** Google Cloud Storage (GCS) - Data Lake
* **Processing Engine:** Databricks (Apache Spark / Delta Lake)
* **Orchestration:** Apache Airflow (Astro CLI)
* **Security:** GCP Secret Manager & Databricks Secret Scopes
* **Language:** Python (PySpark, DAG API)

---

##  The Medallion Pipeline

### ** Bronze: Raw Ingestion**
* **Action:** Ingests raw `.csv` weather records from the GCS landing zone into Delta Lake format.
* **Engineering Detail:** Utilizes **GCP Secret Manager** to securely fetch bucket paths and credentials, ensuring no sensitive information is stored in the source code.

### ** Silver: Data Cleaning**
* **Action:** Performs schema enforcement, handles missing values, and casts data types (e.g., converting temperature observations to floats).
* **Engineering Detail:** Implemented **Idempotent logic**—the task can be re-run multiple times without duplicating data or corrupting the state of the Silver table.

### ** Gold: Business Analytics**
* **Action:** Aggregates data for downstream consumption (e.g., average rainfall per city, historical temperature trends).
* **Engineering Detail:** Optimized tables for high-performance querying and potential BI integration.

---

## Orchestration (Apache Airflow)
The entire workflow is managed by an Airflow **Directed Acyclic Graph (DAG)**. This ensures that the Silver layer only begins after a successful Bronze ingest, and the Gold layer only begins after a successful Silver run.

### **Key Airflow Components Used:**
* **Hooks:** Leveraged the `DatabricksHook` for secure, cross-cloud authentication via Personal Access Tokens (PAT).
* **Operators:** Utilized the `DatabricksRunNowOperator` to trigger modular notebook executions.
* **Error Handling:** Configured task retries and automated logs for high observability.

---

##  Key Engineering Highlights
* **Secure Development Lifecycle (SDLC):** Fully version-controlled via Git with zero hardcoded secrets.
* **Scalability:** Leveraged Databricks' auto-scaling clusters to handle large-scale datasets.
* **Reliability:** Implemented modular task structures, allowing for "restart-from-failure" without re-running the entire pipeline.
