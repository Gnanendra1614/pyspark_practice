# Practice: Using min and max aggregations with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("06_min_max")
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


# Minimum and Maximum salary
salary_range = employees.select(
    min("salary").alias("minimum_salary"),
    max("salary").alias("maximum_salary")
)

print("Minimum and Maximum Salary:")
salary_range.show()


# Minimum and Maximum salary by department
salary_by_department = employees.groupBy(
    "department_id"
).agg(
    min("salary").alias("minimum_salary"),
    max("salary").alias("maximum_salary")
)

print("Minimum and Maximum Salary by Department:")
salary_by_department.show(truncate=False)


# Stop Spark
spark.stop()