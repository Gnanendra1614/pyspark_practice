# Practice: Implementing SCD Type 2 with PySpark
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SCDType2")
    .master("local[*]")
    .getOrCreate()
)

# Existing historical data
existing_df = spark.createDataFrame([
    (1, "Rahul", "Bangalore", "2024-01-01", "9999-12-31", True),
    (2, "Karthik", "Chennai", "2024-01-01", "9999-12-31", True)
], [
    "customer_id",
    "customer_name",
    "city",
    "start_date",
    "end_date",
    "is_current"
])

print("Existing Data:")
existing_df.show()


# New changed data
new_df = spark.createDataFrame([
    (1, "Rahul", "Mumbai")
], [
    "customer_id",
    "customer_name",
    "city"
])

print("New Data:")
new_df.show()


# Close the old record
old_record = existing_df.filter(
    existing_df.customer_id == 1
).withColumn(
    "end_date",
    F.lit("2026-09-30")
).withColumn(
    "is_current",
    F.lit(False)
)

# Create new version
new_record = spark.createDataFrame([
    (1, "Rahul", "Mumbai", "2026-09-30", "9999-12-31", True)
], [
    "customer_id",
    "customer_name",
    "city",
    "start_date",
    "end_date",
    "is_current"
])

print("New Version:")
new_record.show()

spark.stop()