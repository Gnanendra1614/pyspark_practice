# Practice: Handling duplicate columns in joins with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("07_duplicate_columns")
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


# Perform Inner Join
joined_df = e.join(
    d,
    col("e.department_id") == col("d.department_id"),
    "inner"
)


# Select columns and avoid duplicate department_id
result = joined_df.select(
    col("e.employee_id"),
    col("e.employee_name"),
    col("e.department_id"),
    col("e.salary"),
    col("e.city"),
    col("d.department_name")
)


# Display result
print("Join Result Without Duplicate Columns:")
result.show(truncate=False)


# Stop Spark
spark.stop()