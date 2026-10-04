# Practice: Implementing SCD Type 1 with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("SCDType1")
    .master("local[*]")
    .getOrCreate()
)

# Existing customer data
existing_df = spark.createDataFrame([
    (1, "Rahul", "Bangalore"),
    (2, "Karthik", "Chennai"),
    (3, "Praveen", "Hyderabad")
], ["customer_id", "customer_name", "city"])

print("Existing Data:")
existing_df.show()


# New customer data
new_df = spark.createDataFrame([
    (1, "Rahul", "Mumbai"),
    (2, "Karthik", "Chennai"),
    (4, "Manoj", "Delhi")
], ["customer_id", "customer_name", "city"])

print("New Data:")
new_df.show()


# Type 1 concept:
# Old value is replaced by new value.

result = (
    existing_df
    .join(new_df, "customer_id", "left")
    .select(
        "customer_id",
        F.coalesce(
            new_df.customer_name,
            existing_df.customer_name
        ).alias("customer_name"),
        F.coalesce(
            new_df.city,
            existing_df.city
        ).alias("city")
    )
)

print("SCD Type 1 Result:")
result.show()

spark.stop()