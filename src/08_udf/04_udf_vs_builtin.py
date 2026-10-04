# Practice: Comparing UDFs with built-in functions in PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

spark = (
    SparkSession.builder
    .appName("UDFVsBuiltIn")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "rahul"),
    (2, "karthik"),
    (3, "praveen"),
    (4, "manoj")
], ["id", "name"])

print("Original Data:")
df.show()


# -------------------------------
# Using Python UDF
# -------------------------------

def convert_upper(name):
    return name.upper()

upper_udf = F.udf(
    convert_upper,
    StringType()
)

udf_result = df.withColumn(
    "upper_name_udf",
    upper_udf("name")
)

print("Using Python UDF:")
udf_result.show()


# -------------------------------
# Using Built-in Function
# -------------------------------

builtin_result = df.withColumn(
    "upper_name_builtin",
    F.upper("name")
)

print("Using Built-in Function:")
builtin_result.show()


spark.stop()