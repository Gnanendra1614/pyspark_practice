# Practice: Implementing SCD Type 3 with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("SCDType3")
    .master("local[*]")
    .getOrCreate()
)

# Existing data
existing_df = spark.createDataFrame([
    (1, "Rahul", "Bangalore"),
    (2, "Karthik", "Chennai"),
    (3, "Praveen", "Hyderabad")
], ["customer_id", "customer_name", "current_city"])

print("Existing Data:")
existing_df.show()


# New city data
new_df = spark.createDataFrame([
    (1, "Mumbai"),
    (2, "Delhi")
], ["customer_id", "new_city"])

print("New Data:")
new_df.show()


# Apply Type 3 logic
result = (
    existing_df
    .join(new_df, "customer_id", "left")
    .withColumn(
        "previous_city",
        F.when(
            F.col("new_city").isNotNull(),
            F.col("current_city")
        )
    )
    .withColumn(
        "current_city",
        F.coalesce(
            F.col("new_city"),
            F.col("current_city")
        )
    )
    .drop("new_city")
)

print("SCD Type 3 Result:")
result.show()

spark.stop()