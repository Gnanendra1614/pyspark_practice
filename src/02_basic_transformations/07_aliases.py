# Practice: Using aliases transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("07_aliases")
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

# Rename columns using alias()
df.select(
    col("employee_id").alias("Employee_ID"),
    col("employee_name").alias("Employee_Name"),
    col("department").alias("Department"),
    col("salary").alias("Salary")
).show()

# Alias a calculated column
df.select(
    col("employee_name"),
    col("salary"),
    (col("salary") * 12).alias("Annual_Salary")
).show()

spark.stop()