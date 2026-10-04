# Practice: Using when_otherwise transformation with PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Independent SparkSession for this practice file.
spark = (
    SparkSession.builder
    .appName("05_when_otherwise")
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

# Create salary category
df_with_category = df.withColumn(
    "salary_category",
    when(col("salary") >= 80000, "High")
    .when(col("salary") >= 50000, "Medium")
    .otherwise("Low")
)

print("DataFrame with salary category:")
df_with_category.show()

spark.stop()