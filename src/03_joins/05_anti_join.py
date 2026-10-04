# Practice: Using anti join with PySpark
from pyspark.sql import SparkSession


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("05_anti_join")
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


# Perform Left Anti Join
result = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left_anti"
)


# Display result
print("Left Anti Join Result:")
result.show(truncate=False)


# Stop Spark
spark.stop()