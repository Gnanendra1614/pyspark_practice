from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("CheckPartitions")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 65000),
    (5, "Harish", 90000),
    (6, "Naveen", 45000),
    (7, "Sandeep", 70000),
    (8, "Arun", 60000)
]

columns = [
    "employee_id",
    "employee_name",
    "salary"
]

df = spark.createDataFrame(data, columns)

print("Number of partitions:", df.rdd.getNumPartitions())

df.show()

spark.stop()