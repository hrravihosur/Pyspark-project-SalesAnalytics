# Day 12 — Window Functions

Practiced `row_number`, `dense_rank`, running totals and window frames.

```python
win = Window.partitionBy("country").orderBy(col("salary"))
df.withColumn("rn", row_number().over(win))
```

**Project connection:** Window functions were used to keep the latest CDC record per customer.
