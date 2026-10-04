# Practice: Using Python UDFs with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

spark = (
    SparkSession.builder
    .appName("PythonUDF")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul"),
    (2, "Karthik"),
    (3, "Praveen"),
    (4, "Manoj")
], ["id", "name"])

print("Original Data:")
df.show()

# Python function
def convert_upper(name):
    return name.upper()

# Create UDF
upper_udf = F.udf(convert_upper, StringType())

# Apply UDF
result = df.withColumn(
    "upper_name",
    upper_udf("name")
)

print("After Applying UDF:")
result.show()

spark.stop()