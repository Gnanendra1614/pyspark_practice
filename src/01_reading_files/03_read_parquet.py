from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadParquet").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED"

df = (
    spark.read.format("parquet")
    .load(DATA_PATH + r"\DATA.parquet")
)

df.printSchema()
df.show(truncate=False)

spark.stop()
# Practice: Reading Parquet files with PySpark