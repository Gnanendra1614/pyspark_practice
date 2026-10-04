# Practice: Using numeric functions with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("PRACTICE").master("local[*]").getOrCreate()


df = spark.createDataFrame([
    (1, "Aarav", 70000.75),
    (2, "Diya", 85000.45),
    (3, "Kabir", -60000.80),
    (4, "Rohan", 65000.25)
], ["id", "name", "salary"])


df.select(
    F.round("salary", 2).alias("round"),
    F.ceil("salary").alias("ceil"),
    F.floor("salary").alias("floor"),
    F.abs("salary").alias("absolute"),
    F.sqrt("salary").alias("square_root"),
    F.pow("salary", 2).alias("power"),
    F.log("salary").alias("log"),
    F.exp("salary").alias("exponential")
).show(truncate=False)


spark.stop()