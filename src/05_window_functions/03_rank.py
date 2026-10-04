# Practice: Using rank with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, col


spark = (
    SparkSession.builder
    .appName("03_rank")
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


# Assign rank
result = employees.withColumn(
    "salary_rank",
    rank().over(window_spec)
)

print("Salary Rank by Department:")
result.orderBy(
    "department_id",
    "salary_rank"
).show(truncate=False)


spark.stop()