from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Coalesce")
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

repartitioned_df = df.repartition(4)

print("Partitions after repartition:")
print(repartitioned_df.rdd.getNumPartitions())

coalesced_df = repartitioned_df.coalesce(2)

print("Partitions after coalesce:")
print(coalesced_df.rdd.getNumPartitions())

coalesced_df.show()

spark.stop()