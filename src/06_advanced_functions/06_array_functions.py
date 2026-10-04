# Practice: Using array functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = (
    SparkSession.builder
    .appName("PRACTICE")
    .master("local[*]")
    .getOrCreate()
)


df = spark.createDataFrame([
    (1, "Aarav", ["Python", "SQL", "PySpark"]),
    (2, "Diya", ["Python", "SQL"]),
    (3, "Kabir", ["Java", "SQL", "Spark"]),
    (4, "Rohan", ["Python", "Excel"])
], ["id", "name", "skills"])


print("Original Data:")
df.show(truncate=False)


df.select(
    "id",
    "name",
    "skills",

    # Number of elements in array
    F.size("skills").alias("skill_count"),

    # Check whether an array contains a value
    F.array_contains(
        "skills",
        "Python"
    ).alias("has_python"),

    # Get first element
    F.element_at(
        "skills",
        1
    ).alias("first_skill"),

    # Remove duplicate values
    F.array_distinct(
        "skills"
    ).alias("unique_skills"),

    # Sort array
    F.array_sort(
        "skills"
    ).alias("sorted_skills")

).show(truncate=False)


spark.stop()