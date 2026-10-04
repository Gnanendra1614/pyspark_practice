# Practice: Using date and time functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()


df = spark.createDataFrame([
    (1, "Aarav", "2024-01-15", "2024-01-15 10:30:00"),
    (2, "Diya", "2023-06-20", "2023-06-20 14:45:00"),
    (3, "Kabir", "2022-09-10", "2022-09-10 09:15:00"),
    (4, "Rohan", "2025-03-25", "2025-03-25 18:20:00")
], ["id", "name", "joining_date", "joining_timestamp"])


df = df.withColumn(
    "joining_date",
    F.to_date("joining_date")
).withColumn(
    "joining_timestamp",
    F.to_timestamp("joining_timestamp")
)


df.select(
    "id",
    "name",
    "joining_date",

    F.year("joining_date").alias("year"),

    F.month("joining_date").alias("month"),

    F.day("joining_date").alias("day"),

    F.dayofweek("joining_date").alias("day_of_week"),

    F.dayofmonth("joining_date").alias("day_of_month"),

    F.weekofyear("joining_date").alias("week_of_year"),

    F.date_add("joining_date", 10).alias("date_after_10_days"),

    F.date_sub("joining_date", 10).alias("date_before_10_days"),

    F.datediff(
        F.current_date(),
        "joining_date"
    ).alias("days_from_joining"),

    F.add_months(
        "joining_date",
        2
    ).alias("date_after_2_months"),

    F.last_day("joining_date").alias("last_day_of_month"),

    F.current_date().alias("current_date"),

    F.current_timestamp().alias("current_timestamp")
).show(truncate=False)


spark.stop()