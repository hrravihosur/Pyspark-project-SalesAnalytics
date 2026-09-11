# Day 20 — PySpark implementation

The original implementation was developed and validated in Databricks. The snippets below are organized by pipeline stage so they can be adapted to a Databricks notebook or `.py` job.

## 01 — Bronze

```python
project_root = "/Volumes/<catalog>/<schema>/day20"
bronze_customers_initial_path = f"{project_root}/bronze/customers_initial"
bronze_customers_cdc_path = f"{project_root}/bronze/customers_cdc"
bronze_orders_path = f"{project_root}/bronze/orders"

customers_initial_df.write.format("delta").mode("overwrite").save(bronze_customers_initial_path)
customers_cdc_df.write.format("delta").mode("overwrite").save(bronze_customers_cdc_path)
orders_df.write.format("delta").mode("overwrite").save(bronze_orders_path)
```

## 02 — Silver customers: CDC deduplication

```python
from pyspark.sql.functions import col, to_timestamp, trim, upper, row_number
from pyspark.sql.window import Window
from delta.tables import DeltaTable

bronze_cdc = spark.read.format("delta").load(bronze_customers_cdc_path)

silver_cdc = bronze_cdc.withColumn(
    "updated_at",
    to_timestamp(col("updated_at"), "yyyy-MM-dd HH:mm:ss")
)

cdc_window = (
    Window.partitionBy("customer_id")
    .orderBy(col("updated_at").desc())
)

silver_cdc_dedup = (
    silver_cdc
    .withColumn("rn", row_number().over(cdc_window))
    .filter(col("rn") == 1)
    .drop("rn")
)
```

## 03 — Silver customers: Delta MERGE

```python
silver_customers_path = f"{project_root}/silver/customers"

target_table = DeltaTable.forPath(spark, silver_customers_path)

target_table.alias("target").merge(
    silver_cdc_dedup.alias("source"),
    "target.customer_id = source.customer_id"
).whenMatchedUpdate(
    condition="source.operation = 'U'",
    set={
        "customer_name": "source.customer_name",
        "country": "source.country",
        "status": "source.status"
    }
).whenMatchedDelete(
    condition="source.operation = 'D'"
).whenNotMatchedInsert(
    condition="source.operation = 'I'",
    values={
        "customer_id": "source.customer_id",
        "customer_name": "source.customer_name",
        "country": "source.country",
        "status": "source.status"
    }
).execute()
```

## 04 — Silver orders and enrichment

```python
from pyspark.sql.functions import to_date, broadcast

bronze_orders = spark.read.format("delta").load(bronze_orders_path)

silver_orders = (
    bronze_orders
    .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
    .withColumn("category", trim(col("category")))
    .dropDuplicates(["order_id"])
)

silver_orders_path = f"{project_root}/silver/orders"
silver_orders.write.format("delta").mode("overwrite").save(silver_orders_path)

silver_customers = spark.read.format("delta").load(silver_customers_path)
silver_orders = spark.read.format("delta").load(silver_orders_path)

enriched_sales = (
    silver_orders.alias("orders")
    .join(
        silver_customers.alias("customers"),
        col("orders.customer_id") == col("customers.customer_id"),
        "left"
    )
    .select(
        col("orders.order_id"),
        col("orders.customer_id"),
        col("customers.customer_name"),
        col("customers.country"),
        col("customers.status"),
        col("orders.category"),
        col("orders.amount"),
        col("orders.order_date")
    )
)
```

## 05 — Gold aggregations

```python
from pyspark.sql.functions import sum, count, round

sales_by_country = (
    enriched_sales.groupBy("country")
    .agg(
        sum("amount").alias("total_sales"),
        count("order_id").alias("order_count")
    )
    .withColumn("total_sales", round(col("total_sales"), 2))
)

sales_by_category = (
    enriched_sales.groupBy("category")
    .agg(
        sum("amount").alias("total_sales"),
        count("order_id").alias("order_count")
    )
)

customer_sales = (
    enriched_sales.groupBy(
        "customer_id", "customer_name", "country", "status"
    )
    .agg(
        sum("amount").alias("total_sales"),
        count("order_id").alias("order_count")
    )
)
```

## 06 — Reconciliation

```python
from pyspark.sql.functions import sum

enriched_sales.agg(sum("amount").alias("total_sales")).show()
# Expected: 745000

sales_by_country.agg(sum("total_sales").alias("total_sales")).show()
# Expected: 745000
```

> Note: the project uses placeholder storage paths so the code can be adapted to another Databricks environment without exposing environment-specific paths.
