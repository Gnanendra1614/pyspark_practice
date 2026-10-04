# Practice: Using partitionBy with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import max


spark = (
    SparkSession.builder
    .appName("Window_partitionBy")
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


# Window using partitionBy()
window_spec = Window.partitionBy("department_id")


# Maximum salary within each department
result = employees.withColumn(
    "department_max_salary",
    max("salary").over(window_spec)
)

print("Using Window.partitionBy():")
result.show(truncate=False)

spark.stop()