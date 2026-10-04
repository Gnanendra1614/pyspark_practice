# Practice: Writing CSV files with PySpark
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("WriteCSV")
    .master("local[*]")
    .getOrCreate()
)

# Create DataFrame
df = spark.createDataFrame([
    (1, "Rahul", "IT", 75000),
    (2, "Karthik", "HR", 55000),
    (3, "Praveen", "Finance", 85000),
    (4, "Manoj", "Sales", 65000)
], ["employee_id", "employee_name", "department", "salary"])

print("Original Data:")
df.show()

# Write DataFrame to CSV
df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(r".\output\employees_csv")

print("CSV file written successfully!")

spark.stop()