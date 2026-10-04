# Practice: Using count aggregation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import count


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("03_count")
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


# Total number of employees
total_employees = employees.select(
    count("*").alias("total_employees")
)


print("Total Employees:")
total_employees.show()


# Count employees by department
employees_by_department = employees.groupBy(
    "department_id"
).agg(
    count("*").alias("employee_count")
)


print("Employees by Department:")
employees_by_department.show(truncate=False)


# Stop Spark
spark.stop()