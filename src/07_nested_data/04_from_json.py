# Practice: Using from_json with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType

spark = (
    SparkSession.builder
    .appName("FromJSON")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, '{"city":"Bangalore","experience":2}'),
    (2, '{"city":"Chennai","experience":3}'),
    (3, '{"city":"Hyderabad","experience":1}')
], ["id", "details"])

print("Original JSON Data:")
df.show(truncate=False)

# JSON Schema
json_schema = StructType([
    StructField("city", StringType(), True),
    StructField("experience", IntegerType(), True)
])

# Convert JSON string into Struct
result = df.withColumn(
    "details_struct",
    F.from_json("details", json_schema)
)

print("Parsed JSON:")
result.show(truncate=False)

spark.stop()