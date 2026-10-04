# Practice: Using join conditions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("06_join_condition")
    .master("local[*]")
    .getOrCreate()
)


# Data folder path
DATA_PATH = r".\Data"


# Read employees.csv
employees = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(DATA_PATH + r"\employees.csv")
)


# Read departments.csv
departments = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(DATA_PATH + r"\departments.csv")
)


# Create aliases
e = employees.alias("e")
d = departments.alias("d")


# Join using explicit join condition
result = e.join(
    d,
    col("e.department_id") == col("d.department_id"),
    "inner"
)


# Select required columns
result = result.select(
    col("e.employee_id"),
    col("e.employee_name"),
    col("e.department_id"),
    col("e.salary"),
    col("e.city"),
    col("d.department_name")
)


# Display result
print("Join Condition Result:")
result.show(truncate=False)


# Stop Spark
spark.stop()