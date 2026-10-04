from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadJSON").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED"

df = (
    spark.read.format("json")
    .option("inferSchema", True)
    .load(DATA_PATH + r"\DATA.json")
)

df.printSchema()
df.show(truncate=False)

spark.stop()
# Practice: Reading JSON files with PySpark