# Practice: Using UDFs with conditions in PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

spark = (
    SparkSession.builder
    .appName("UDFCondition")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame([
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 45000)
], ["id", "name", "salary"])

print("Original Data:")
df.show()


# Python function with condition
def salary_category(salary):

    if salary >= 80000:
        return "High"

    elif salary >= 50000:
        return "Medium"

    else:
        return "Low"


# Create UDF
salary_udf = F.udf(
    salary_category,
    StringType()
)


# Apply UDF
result = df.withColumn(
    "salary_category",
    salary_udf("salary")
)

print("After Applying Conditional UDF:")
result.show()

spark.stop()