# Practice: Using orderBy with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col


spark = (
    SparkSession.builder
    .appName("Window_orderBy")
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


# Window using orderBy()
window_spec = Window.orderBy(
    col("salary").desc()
)


# Assign row number based on salary
result = employees.withColumn(
    "salary_row_number",
    row_number().over(window_spec)
)

print("Using Window.orderBy():")
result.show(truncate=False)

spark.stop()