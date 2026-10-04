# Practice: Using explode with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("Explode")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul", ["Python", "SQL", "PySpark"]),
    (2, "Karthik", ["Java", "SQL"]),
    (3, "Praveen", ["Python", "Spark"])
], ["id", "name", "skills"])

print("Original Data:")
df.show(truncate=False)

print("Exploded Data:")

result = df.select(
    "id",
    "name",
    F.explode("skills").alias("skill")
)

result.show()

spark.stop()