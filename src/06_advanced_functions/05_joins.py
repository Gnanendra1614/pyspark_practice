# Practice: Using joins with PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("Joins")
    .master("local[*]")
    .getOrCreate()
)

# Employee Data
employees = spark.createDataFrame([
    (1, "Rahul", 101, 75000),
    (2, "Karthik", 102, 55000),
    (3, "Praveen", 103, 85000),
    (4, "Manoj", 104, 65000),
    (5, "Harish", 101, 90000),
    (6, "Naveen", 105, 45000)
], ["employee_id", "employee_name", "department_id", "salary"])


# Department Data
departments = spark.createDataFrame([
    (101, "IT"),
    (102, "HR"),
    (103, "Finance"),
    (104, "Sales"),
    (105, "Marketing"),
    (106, "Operations")
], ["department_id", "department_name"])


print("Employees:")
employees.show()

print("Departments:")
departments.show()


# 1. INNER JOIN
inner_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "inner"
)

print("INNER JOIN:")
inner_join.show()


# 2. LEFT JOIN
left_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left"
)

print("LEFT JOIN:")
left_join.show()


# 3. RIGHT JOIN
right_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "right"
)

print("RIGHT JOIN:")
right_join.show()


# 4. FULL OUTER JOIN
full_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "full"
)

print("FULL OUTER JOIN:")
full_join.show()


# 5. LEFT SEMI JOIN
left_semi_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left_semi"
)

print("LEFT SEMI JOIN:")
left_semi_join.show()


# 6. LEFT ANTI JOIN
left_anti_join = employees.join(
    departments,
    employees.department_id == departments.department_id,
    "left_anti"
)

print("LEFT ANTI JOIN:")
left_anti_join.show()


# 7. JOIN WITH CONDITION
condition_join = employees.join(
    departments,
    (employees.department_id == departments.department_id)
    & (employees.salary > 60000),
    "inner"
)

print("JOIN WITH CONDITION:")
condition_join.show()


spark.stop()