# Practice: Using left join with PySpark
from pyspark.sql import SparkSession


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("02_left_join")
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


# Display Employees table
print("Employees Table:")
employees.show(truncate=False)


# Display Departments table
print("Departments Table:")
departments.show(truncate=False)


# Perform Left Join
result = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left"
)


# Select required columns
result = result.select(
    employees.employee_id,
    employees.employee_name,
    employees.department_id,
    employees.salary,
    employees.city,
    departments.department_name
)


# Display Left Join result
print("Left Join Result:")
result.show(truncate=False)


# Stop Spark
spark.stop()