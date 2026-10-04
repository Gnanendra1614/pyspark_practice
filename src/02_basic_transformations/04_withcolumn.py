# Practice: Using withcolumn transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("04_withColumn")
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

# Create a new column
df_with_column = df.withColumn(
    "annual_salary",
    col("salary") * 12
)

print("DataFrame with annual salary:")
df_with_column.show()

spark.stop()