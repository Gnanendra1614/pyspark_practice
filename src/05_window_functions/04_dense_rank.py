# Practice: Using dense_rank with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank, col

spark = (
    SparkSession.builder
    .appName("04_dense_rank")
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

# Apply dense_rank
result = employees.withColumn(
    "salary_dense_rank",
    dense_rank().over(window_spec)
)

print("Dense Rank by Department:")

result.orderBy(
    "department_id",
    "salary_dense_rank"
).show(truncate=False)

spark.stop()