# Practice: Using groupBy with multiple columns in PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum

spark = (
    SparkSession.builder
    .appName("08_groupby_multiple_columns")
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

# Group by department and city
result = employees.groupBy(
    "department_id",
    "city"
).agg(
    count("*").alias("employee_count"),
    sum("salary").alias("total_salary")
)

print("Employee Count and Total Salary by Department and City:")

result.orderBy(
    "department_id",
    "city"
).show(truncate=False)

spark.stop()