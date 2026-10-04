# Practice: Using UDFs with multiple columns in PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

spark = (
    SparkSession.builder
    .appName("UDFMultipleColumns")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul", "IT"),
    (2, "Karthik", "HR"),
    (3, "Praveen", "Finance"),
    (4, "Manoj", "Sales")
], ["id", "name", "department"])

print("Original Data:")
df.show()

# Python function using multiple columns
def create_info(name, department):
    return name + " - " + department

# Create UDF
info_udf = F.udf(create_info, StringType())

# Apply UDF
result = df.withColumn(
    "employee_info",
    info_udf("name", "department")
)

print("After Applying UDF:")
result.show()

spark.stop()