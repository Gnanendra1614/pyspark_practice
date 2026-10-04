# Practice: Using groupBy with PySpark
from pyspark.sql import SparkSession


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("02_group_by")
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


# Display Employees table
print("Employees Table:")
employees.show(truncate=False)


# Group employees by department
result = employees.groupBy("department_id").count()


# Display result
print("Employee Count by Department:")
result.show(truncate=False)


# Stop Spark
spark.stop()