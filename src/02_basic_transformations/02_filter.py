# Practice: Using filter transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("02_filter")
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

# Filter employees whose salary is greater than 50000
filtered_df = df.filter(col("salary") > 50000)

print("Employees with salary greater than 50000:")
filtered_df.show()

# Filter employees from a specific department
department_df = df.filter(col("department") == "IT")

print("Employees from IT department:")
department_df.show()

spark.stop()