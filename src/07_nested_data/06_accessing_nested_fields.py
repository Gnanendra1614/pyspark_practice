# Practice: Accessing nested fields with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("AccessingNestedFields")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (
        1,
        "Rahul",
        ("Bangalore", 560001)
    ),
    (
        2,
        "Karthik",
        ("Chennai", 600001)
    ),
    (
        3,
        "Praveen",
        ("Hyderabad", 500001)
    )
], ["id", "name", "address"])

# Convert address into a Struct
result = df.select(
    "id",
    "name",
    F.struct(
        F.col("address._1").alias("city"),
        F.col("address._2").alias("pincode")
    ).alias("address_info")
)

print("Nested Data:")
result.show(truncate=False)


# Access nested fields
print("Accessing Nested Fields:")

result.select(
    "id",
    "name",
    F.col("address_info.city").alias("city"),
    F.col("address_info.pincode").alias("pincode")
).show()


spark.stop()