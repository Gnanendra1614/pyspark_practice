from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Repartition")
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

print("Original partitions:")
print(df.rdd.getNumPartitions())

repartitioned_df = df.repartition(4)

print("Partitions after repartition:")
print(repartitioned_df.rdd.getNumPartitions())

repartitioned_df.show()

spark.stop()