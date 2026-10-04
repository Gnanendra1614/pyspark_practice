# Practice: Using row_number with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col


spark = (
    SparkSession.builder
    .appName("02_row_number")
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


# Create window
window_spec = Window.partitionBy(
    "department_id"
).orderBy(
    col("salary").desc()
)


# Assign row number
result = employees.withColumn(
    "row_number",
    row_number().over(window_spec)
)

print("Row Number by Department:")
result.orderBy(
    "department_id",
    "row_number"
).show(truncate=False)


spark.stop()