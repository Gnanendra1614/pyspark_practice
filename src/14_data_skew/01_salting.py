from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("DataSkewSalting")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", "IT"),
    (2, "Karthik", "IT"),
    (3, "Praveen", "IT"),
    (4, "Manoj", "IT"),
    (5, "Harish", "IT"),
    (6, "Naveen", "HR"),
    (7, "Sandeep", "Finance"),
    (8, "Arun", "Sales")
]

columns = ["employee_id", "employee_name", "department"]

df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()

print("Department Distribution:")
df.groupBy("department").count().show()

# Add salt value
salted_df = df.withColumn(
    "salt",
    (F.rand() * 5).cast("int")
)

print("Data After Adding Salt:")
salted_df.show()

# Create salted key
salted_df = salted_df.withColumn(
    "salted_department",
    F.concat_ws("_", "department", "salt")
)

print("Data With Salted Key:")
salted_df.show()

spark.stop()