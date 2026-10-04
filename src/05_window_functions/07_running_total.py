# Practice: Calculating running totals with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import sum, col

spark = (
    SparkSession.builder
    .appName("07_running_total")
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

# Window by department and order by salary
window_spec = (
    Window
    .partitionBy("department_id")
    .orderBy(col("salary").desc())
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)
)

# Running total salary
result = employees.withColumn(
    "running_total_salary",
    sum("salary").over(window_spec)
)

print("Running Total Salary by Department:")

result.orderBy(
    "department_id",
    col("salary").desc()
).show(truncate=False)

spark.stop()