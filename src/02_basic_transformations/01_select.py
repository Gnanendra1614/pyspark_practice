# Practice: Using select transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
    .appName("01_select")
    .master("local[*]")
    .getOrCreate()
)

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED\DATA.csv"

df = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .load(DATA_PATH)
)

print("Original DataFrame:")
df.show()

print("Columns:")
print(df.columns)

# Select specific columns
selected_df = df.select(
    "employee_id",
    "employee_name",
    "department",
    "salary"
)

print("Selected columns:")
selected_df.show()

# Select using column expressions
df.select(
    col("employee_name"),
    col("salary")
).show()

spark.stop()