# Practice: Parsing nested JSON with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    ArrayType
)

spark = (
    SparkSession.builder
    .appName("NestedJSONParsing")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (
        1,
        '{"name":"Rahul","address":{"city":"Bangalore","pincode":560001},"skills":["Python","SQL","PySpark"]}'
    ),
    (
        2,
        '{"name":"Karthik","address":{"city":"Chennai","pincode":600001},"skills":["Java","SQL"]}'
    )
], ["id", "details"])

print("Original Data:")
df.show(truncate=False)


# Address Schema
address_schema = StructType([
    StructField("city", StringType(), True),
    StructField("pincode", IntegerType(), True)
])


# Complete JSON Schema
json_schema = StructType([
    StructField("name", StringType(), True),
    StructField("address", address_schema, True),
    StructField("skills", ArrayType(StringType()), True)
])


# Parse JSON
result = df.withColumn(
    "details_struct",
    F.from_json("details", json_schema)
)

print("Parsed Nested JSON:")
result.show(truncate=False)


# Access nested fields
result.select(
    "id",
    "details_struct.name",
    "details_struct.address.city",
    "details_struct.address.pincode",
    "details_struct.skills"
).show(truncate=False)


spark.stop()