# Practice: Using sum aggregation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("04_sum")
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


# Total salary of all employees
total_salary = employees.select(
    sum("salary").alias("total_salary")
)

print("Total Salary:")
total_salary.show()


# Total salary by department
salary_by_department = employees.groupBy(
    "department_id"
).agg(
    sum("salary").alias("total_salary")
)

print("Total Salary by Department:")
salary_by_department.show(truncate=False)


# Stop Spark
spark.stop()