# Practice: Working with arrays in PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("Arrays")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul", ["Python", "SQL", "PySpark"]),
    (2, "Karthik", ["Java", "SQL"]),
    (3, "Praveen", ["Python", "Spark"]),
    (4, "Manoj", ["SQL", "Excel"])
], ["id", "name", "skills"])

print("Original Data:")
df.show(truncate=False)

print("Array Functions:")

df.select(
    "id",
    "name",
    "skills",
    F.size("skills").alias("skill_count"),
    F.array_contains("skills", "Python").alias("has_python"),
    F.element_at("skills", 1).alias("first_skill"),
    F.array_distinct("skills").alias("unique_skills"),
    F.array_sort("skills").alias("sorted_skills")
).show(truncate=False)

spark.stop()