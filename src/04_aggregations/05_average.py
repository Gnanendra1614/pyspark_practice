# Practice: Using average aggregation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


# Create Spark Session
spark = (
    SparkSession.builder
    .appName("05_avg")
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


# Average salary of all employees
average_salary = employees.select(
    avg("salary").alias("average_salary")
)

print("Average Salary:")
average_salary.show()


# Average salary by department
average_by_department = employees.groupBy(
    "department_id"
).agg(
    avg("salary").alias("average_salary")
)

print("Average Salary by Department:")
average_by_department.show(truncate=False)


# Stop Spark
spark.stop()