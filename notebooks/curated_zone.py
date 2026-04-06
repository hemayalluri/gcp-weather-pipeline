# Databricks notebook source
# Databricks notebook source
from pyspark.sql.functions import avg, sum, round, year, month

# 1. Load the clean data from Silver
silver_df = spark.read.table("weather_analysis.silver_weather_cleaned")

# 2. Add Time Features and Aggregate
gold_df = (silver_df
    .withColumn("year", year("date"))
    .withColumn("month", month("date"))
    .groupBy("location", "year", "month")
    .agg(
        round(avg("maxtemp"), 2).alias("avg_max_temp"),
        round(sum("rainfall"), 2).alias("total_monthly_rainfall")
    )
    .orderBy("year", "month", "location")
)

# 3. Save as the Gold Delta Table
gold_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("weather_analysis.gold_weather_summary")

print("Curated table 'gold_weather_summary' is now LIVE!")