# Practice: Working with structs in PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("Structs")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 65000)
], ["id", "name", "salary"])

print("Original Data:")
df.show()

# Create Struct
result = df.select(
    "id",
    F.struct(
        F.col("name").alias("employee_name"),
        F.col("salary").alias("employee_salary")
    ).alias("employee_info")
)

print("Struct Data:")
result.show(truncate=False)

spark.stop()