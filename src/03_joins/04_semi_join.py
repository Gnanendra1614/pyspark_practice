# Practice: Using semi join with PySpark
from pyspark.sql import SparkSession


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("04_semi_join")
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


# Perform Left Semi Join
result = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left_semi"
)


# Display result
print("Left Semi Join Result:")
result.show(truncate=False)


# Stop Spark
spark.stop()