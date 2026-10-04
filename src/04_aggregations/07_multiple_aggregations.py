# Practice: Using multiple aggregations with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    count,
    sum,
    avg,
    min,
    max
)


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("07_multiple_aggregations")
    .master("local[*]")
    .getOrCreate()
)


# Data folder path
DATA_PATH = r".\src\Data"


# Read employees.csv
employees = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(DATA_PATH + r"\employees.csv")
)


# Multiple aggregations by department
result = employees.groupBy(
    "department_id"
).agg(
    count("*").alias("employee_count"),
    sum("salary").alias("total_salary"),
    avg("salary").alias("average_salary"),
    min("salary").alias("minimum_salary"),
    max("salary").alias("maximum_salary")
)


# Display result
print("Multiple Aggregations by Department:")
result.show(truncate=False)


# Stop Spark
spark.stop()