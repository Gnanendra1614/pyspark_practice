# Practice: Using aggregation functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()


df = spark.createDataFrame([
    (1, "Aarav", "Data", 70000, "Python"),
    (2, "Diya", "Data", 85000, "PySpark"),
    (3, "Kabir", "HR", 60000, "Python"),
    (4, "Rohan", "HR", 65000, "SQL"),
    (5, "Rahul", "Data", 75000, "SQL")
], ["id", "name", "department", "salary", "skill"])


df.groupBy("department").agg(

    F.count("*").alias("employee_count"),

    F.sum("salary").alias("total_salary"),

    F.avg("salary").alias("average_salary"),

    F.min("salary").alias("minimum_salary"),

    F.max("salary").alias("maximum_salary"),

    F.countDistinct("skill").alias("unique_skills"),

    F.collect_list("skill").alias("all_skills"),

    F.collect_set("skill").alias("unique_skill_list"),

    F.first("name").alias("first_employee"),

    F.last("name").alias("last_employee")

).show(truncate=False)


spark.stop()