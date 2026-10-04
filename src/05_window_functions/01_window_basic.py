# Practice: Using basic window functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import max


spark = (
    SparkSession.builder
    .appName("01_window_basic")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r".\src\Data"

employees = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(DATA_PATH + r"\employees.csv")
)

print("Employees Table:")
employees.show(truncate=False)


# Define Window
window_spec = Window.partitionBy("department_id")


# Find maximum salary in each department
result = employees.withColumn(
    "department_max_salary",
    max("salary").over(window_spec)
)

print("Maximum Salary in Each Department:")
result.show(truncate=False)


spark.stop()