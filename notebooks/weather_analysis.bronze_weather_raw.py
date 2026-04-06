# Databricks notebook source
# 1. Sourcing from GCP
raw_path = "gs://yalluri-raw-landing-zone/weatherAUS.csv"

# 2. Reading the CSV file
df_raw = (spark.read.format("csv")
          .option("header", "true")
          .option("inferSchema", "true")
          .load(raw_path))

# 3. Write to Bronze Table
df_raw.write.mode("overwrite").saveAsTable("weather_analysis.bronze_weather_raw")

print("Bronze table 'weather_analysis.bronze_weather_raw' is now LIVE!")