# Practice: Using column_expressions transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("06_column_expressions")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\DATA.csv"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(DATA_PATH)
)

print("Original DataFrame:")
df.show()

# Salary calculation
df.select(
    col("employee_name"),
    col("salary"),
    (col("salary") * 12).alias("annual_salary")
).show()

# 10% salary increment
df.select(
    col("employee_name"),
    col("salary"),
    (col("salary") * 1.10).alias("updated_salary")
).show()

spark.stop()