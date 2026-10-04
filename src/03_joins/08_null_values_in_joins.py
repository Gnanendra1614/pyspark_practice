# Practice: Handling null values in joins with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("08_null_values_in_joins")
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


# Perform Left Join
joined_df = e.join(
    d,
    col("e.department_id") == col("d.department_id"),
    "left"
)


# Handle NULL values
result = joined_df.select(
    col("e.employee_id"),
    col("e.employee_name"),
    col("e.department_id"),
    col("e.salary"),
    col("e.city"),
    when(
        col("d.department_name").isNull(),
        "Unknown"
    ).otherwise(
        col("d.department_name")
    ).alias("department_name")
)


# Display result
print("NULL Values Handled:")
result.show(truncate=False)


# Stop Spark
spark.stop()