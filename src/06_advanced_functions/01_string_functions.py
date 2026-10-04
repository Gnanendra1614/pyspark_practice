# Practice: Using string functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()


df = spark.createDataFrame([
    (1, "Aarav", "Data", 70000, ["Python", "SQL"]),
    (2, "Diya", "Data", 85000, ["PySpark", "SQL"]),
    (3, "Kabir", "HR", 60000, ["Python", "Spark"]),
    (4, "Rohan", "HR", 65000, ["SQL", "Excel"])
], ["id", "name", "department", "salary", "skills"])


df.select(
    F.trim("name").alias("trimmed"),
    F.upper("name").alias("upper"),
    F.lower("name").alias("lower"),
    F.length("name").alias("length"),
    F.concat(F.trim("name"), F.lit(" - "), "department").alias("concat"),
    F.concat_ws(" - ", F.trim("name"), "department").alias("concat_ws"),
    F.substring("name", 1, 3).alias("substring"),
    F.split(F.trim("name"), " ").alias("split"),
    F.regexp_replace("department", "Data", "IT").alias("regexp_replace"),
    F.regexp_extract("name", "^(.)", 1).alias("regexp_extract")
).show(truncate=False)


spark.stop()