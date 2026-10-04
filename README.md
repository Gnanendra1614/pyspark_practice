# PySpark Practice

A structured PySpark learning and practice repository covering Spark fundamentals, file handling, transformations, joins, aggregations, window functions, advanced functions, nested data, UDFs, SCD, built-in functions, applyInPandas, and Medallion Architecture.

---

##  Project Overview

This repository contains hands-on PySpark programs created while learning Apache Spark and Data Engineering concepts.

The project follows a topic-by-topic approach, where each concept is implemented using a separate Python program for easy understanding and practice.

---

##  Technologies Used

- Python
- PySpark
- Apache Spark
- Pandas
- SQL
- Delta Lake
- Git & GitHub

---

# PySpark Practice

## Project Structure

```text
pyspark_practice-main/
│
├── README.md
│
├── src/
│   │
│   ├── 00_spark_basics/
│   │   ├── 01_spark_session.py
│   │   ├── 02_create_dataframe.py
│   │   ├── 03_dataframe_schema.py
│   │   ├── 04_show_collect.py
│   │   └── 05_explicit_schema.py
│   │
│   ├── 01_reading_files/
│   │   ├── 01_read_csv.py
│   │   ├── 02_read_json.py
│   │   ├── 03_read_parquet.py
│   │   └── 04_read_delta.py
│   │
│   ├── 01_writing_files/
│   │   ├── 01_write_csv.py
│   │   ├── 02_write_json.py
│   │   ├── 03_write_parquet.py
│   │   └── 04_write_delta.py
│   │
│   ├── 02_basic_transformations/
│   │   ├── 01_select.py
│   │   ├── 02_filter.py
│   │   ├── 03_where.py
│   │   ├── 04_withcolumn.py
│   │   ├── 05_when_otherwise.py
│   │   ├── 06_column_expressions.py
│   │   └── 07_aliases.py
│   │
│   ├── 03_joins/
│   │   ├── 01_inner_join.py
│   │   ├── 02_left_join.py
│   │   ├── 03_outer_join.py
│   │   ├── 04_semi_join.py
│   │   ├── 05_anti_join.py
│   │   ├── 06_join_condition.py
│   │   ├── 07_duplicate_columns.py
│   │   └── 08_null_values_in_joins.py
│   │
│   ├── 04_aggregations/
│   │   ├── 01_import_functions.py
│   │   ├── 02_group_by.py
│   │   ├── 03_count.py
│   │   ├── 04_sum.py
│   │   ├── 05_average.py
│   │   ├── 06_min_and_max.py
│   │   ├── 07_multiple_aggregations.py
│   │   └── 08_groupby_multiple_columns.py
│   │
│   ├── 05_window_functions/
│   │   ├── 01_window_basic.py
│   │   ├── 02_row_number.py
│   │   ├── 03_rank.py
│   │   ├── 04_dense_rank.py
│   │   ├── 05_lag().py
│   │   ├── 06_lead().py
│   │   ├── 07_running_total.py
│   │   ├── 08_partitionby.py
│   │   └── 09_orderby.py
│   │
│   ├── 06_advanced_functions/
│   │   ├── 01_string_functions.py
│   │   ├── 02_numeric_functions.py
│   │   ├── 03_date_time_functions.py
│   │   ├── 04_aggregation_functions.py
│   │   ├── 05_joins.py
│   │   └── 06_array_functions.py
│   │
│   ├── 07_nested_data/
│   │   ├── 01_arrays.py
│   │   ├── 02_structs.py
│   │   ├── 03_explode.py
│   │   ├── 04_from_json.py
│   │   ├── 05_nested_json_parsing.py
│   │   └── 06_accessing_nested_fields.py
│   │
│   ├── 08_udf/
│   │   ├── 01_python_udf.py
│   │   ├── 02_udf_with_multiple_columns.py
│   │   ├── 03_udf_condition.py
│   │   └── 04_udf_vs_builtin.py
│   │
│   ├── 09_scd/
│   │   ├── 01_type_1.py
│   │   ├── 02_type_2.py
│   │   └── 03_type_3.py
│   │
│   ├── 10_built_in_functions/
│   │   ├── 01_limit_function.py
│   │   ├── 02_where_function.py
│   │   ├── 03_like_function.py
│   │   ├── 04_withColumnRenamed_function.py
│   │   ├── 05_drop_function.py
│   │   ├── 06_distinct_function.py
│   │   ├── 07_dropDuplicates_function.py
│   │   ├── 08_sort_function.py
│   │   ├── 09_fillna_function.py
│   │   ├── 10_dropna_function.py
│   │   ├── 11_union_function.py
│   │   ├── 12_unionAll_function.py
│   │   └── 13_pivot_function.py
│   │
│   ├── 11_applyinpandas/
│   │   └── 01_applyinpandas_function.py
│   │
│   ├── 12_medallion_architeture/
│   │   └── 01_medallion_architecture_implementation.py
│   │
│   ├── 13_partitions/
│   │   ├── 01__check_no_of_partitions.py
│   │   ├── 02_repartition.py
│   │   └── 03_coalesce.py
│   │
│   ├── 14_data_skew/
│   │   └── 01_salting.py
│   │
│   └── data/
│       ├── departments.csv
│       └── employees.csv
