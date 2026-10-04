# Practice: Using where transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("03_where")
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

# Filter using where()
filtered_df = df.where(col("salary") > 50000)

print("Employees with salary greater than 50000:")
filtered_df.show()

# Multiple conditions
filtered_df = df.where(
    (col("salary") > 50000) & (col("city") == "Bangalore")
)

print("Employees with salary greater than 50000 from Bangalore:")
filtered_df.show()

spark.stop()