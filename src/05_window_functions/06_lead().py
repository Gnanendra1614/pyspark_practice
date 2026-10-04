# Practice: Using lead with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import lead, col

spark = (
    SparkSession.builder
    .appName("06_lead")
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

# Window: separate by department and order by salary
window_spec = Window.partitionBy(
    "department_id"
).orderBy(
    col("salary").desc()
)

# Get next employee's salary
result = employees.withColumn(
    "next_salary",
    lead("salary", 1).over(window_spec)
)

print("Next Salary by Department:")

result.orderBy(
    "department_id",
    col("salary").desc()
).show(truncate=False)

spark.stop()