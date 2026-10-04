# Practice: Reading Delta files with PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadDelta").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED"

df = (
    spark.read.format("delta")
    .load(DATA_PATH + r"\DATA_delta")
)

df.printSchema()
df.show(truncate=False)

spark.stop()
