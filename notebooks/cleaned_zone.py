# Databricks notebook source
# Databricks notebook source
from pyspark.sql.functions import col, to_date, when

# 1. Loading the raw data from Bronze
bronze_df = spark.read.table("weather_analysis.bronze_weather_raw")

# 2. Transform and Clean
silver_df = (bronze_df
    .withColumn("date", to_date(col("Date"), "yyyy-MM-dd"))
    .withColumn("mintemp", when(col("MinTemp") == "NA", None).otherwise(col("MinTemp")).cast("double"))
    .withColumn("maxtemp", when(col("MaxTemp") == "NA", None).otherwise(col("MaxTemp")).cast("double"))
    .withColumn("rainfall", when(col("Rainfall") == "NA", None).otherwise(col("Rainfall")).cast("double"))
    .select(
        "date", 
        col("Location").alias("location"), 
        "mintemp", 
        "maxtemp", 
        "rainfall",
        col("RainTomorrow").alias("rain_tomorrow")
    )
    .dropna(subset=["date", "location"])
)

# 3. Save as the Silver Delta Table
silver_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("weather_analysis.silver_weather_cleaned")

print("Silver table 'silver_weather_cleaned' is now ready!")