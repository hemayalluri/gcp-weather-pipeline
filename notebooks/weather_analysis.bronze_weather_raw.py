# Databricks notebook source
# 1. Fetch the path SECURELY from the Secret Scope
# The scope is 'gcp-secrets' and the key is 'landing-zone-path'
raw_path = dbutils.secrets.get(scope="gcp-secrets", key="landing-zone-path")

# Print it to verify (Databricks will redact it with [REDACTED] for security)
print(f"Path retrieved successfully: {raw_path}")

# 2. Reading the CSV file
df_raw = (spark.read.format("csv")
          .option("header", "true")
          .option("inferSchema", "true")
          .load(raw_path))

# 3. Write to Bronze Table
df_raw.write.mode("overwrite").saveAsTable("weather_analysis.bronze_weather_raw")

print("Bronze ingestion complete!")