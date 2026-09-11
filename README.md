# PySpark Data Engineering — 20-Day Learning Journey

A hands-on 20-day learning journey focused on **Python, PySpark, Apache Spark, Delta Lake, CDC, Spark optimization, and Azure Data Engineering patterns**.

This repository documents the concepts, practical exercises, and an end-to-end **Customer Sales Analytics** project built using a production-oriented Medallion Architecture.

## 🚀 Skills Covered

- Python fundamentals and advanced concepts
- PySpark and Spark DataFrames
- Spark SQL
- Transformations and actions
- Joins and window functions
- Aggregations, pivot, rollup, and cube
- Spark architecture: jobs, stages, tasks, executors, DAGs
- Partitioning and shuffle
- Spark performance optimization
- Delta Lake
- CDC and Delta MERGE / UPSERT
- Deduplication and idempotency
- Medallion Architecture
- Data quality and reconciliation
- Azure Data Factory orchestration
- ADLS Gen2 concepts
- Power BI integration patterns

## 📚 20-Day Learning Journey

| Day | Topic | Status |
|---|---|---|
| 01 | Python Fundamentals | ✅ |
| 02 | Python Advanced Concepts | ✅ |
| 03 | PySpark Fundamentals | ✅ |
| 04 | Spark Architecture Deep Dive | ✅ |
| 05 | DataFrames and Spark Concepts | ✅ |
| 06 | Schema, Read and Write | ✅ |
| 07 | DataFrame Transformations | ✅ |
| 08 | PySpark Functions | ✅ |
| 09 | Dates and Null Handling | ✅ |
| 10 | Aggregations | ✅ |
| 11 | Joins | ✅ |
| 12 | Window Functions | ✅ |
| 13 | Spark SQL | ✅ |
| 14 | Lazy Evaluation | ✅ |
| 15 | DAG, Jobs, Stages, Tasks and Executors | ✅ |
| 16 | Partitioning | ✅ |
| 17 | Spark Optimization | ✅ |
| 18 | Read / Write and Delta Concepts | ✅ |
| 19 | Delta Lake, CDC and MERGE | ✅ |
| 20 | End-to-End Data Engineering Project | ✅ |

## 🏗️ Day 20 — Customer Sales Analytics

The final project combines the concepts learned throughout the journey into an Azure-style data engineering pipeline.

```text
CRM / ERP
    ↓
Azure Data Factory
    ↓
ADLS Gen2 — Landing
    ↓
Bronze Delta — Raw
    ↓
Databricks / PySpark
    ↓
Silver Delta — Clean / Conformed
    ↓
Gold Delta — Business Ready
    ↓
Power BI
```

### Project capabilities

- CRM customer ingestion
- ERP order ingestion
- Bronze raw-data preservation
- Customer CDC processing: Insert / Update / Delete
- Window-function based CDC deduplication
- Delta MERGE / UPSERT
- Idempotent incremental processing
- Order validation and deduplication
- Customer-order integration using LEFT JOIN
- Preservation of historical transactions for deleted customers
- Gold business aggregations
- Data-quality checks
- Business reconciliation
- Spark performance optimization patterns
- ADF orchestration and parameterization concepts

### Gold datasets

1. **Sales by Country**
2. **Sales by Category**
3. **Customer Sales Summary**

### Business validation

The sample project contains 12 orders with total sales of **₹745,000**. Silver and Gold reconciliation checks preserve the same total, demonstrating that transaction value was not lost during processing.

## 🥉 Bronze → 🥈 Silver → 🥇 Gold

### Bronze

Raw source data with minimal transformation and ingestion metadata.

### Silver

Validated, standardized, deduplicated and conformed data. CDC changes are applied to the current customer state using Delta MERGE.

### Gold

Business-ready aggregations designed for analytics and Power BI consumption.

## ⚡ Optimization Techniques

- Predicate pushdown
- Partition pruning
- Broadcast joins
- Adaptive Query Execution (AQE)
- Data-skew handling / salting
- Appropriate shuffle partitioning
- Cache / persist when justified
- Small-file optimization
- Incremental processing

## 📂 Repository Structure

```text
pyspark-data-engineering-20-days/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── architecture/
│   ├── infographics/
│   └── screenshots/
│
├── days/
│   ├── day01-python-basics/
│   ├── day02-python-advanced/
│   ├── ...
│   ├── day19-delta-cdc/
│   └── day20-end-to-end-project/
│
└── sql/
```

## 🎯 Learning Philosophy

The goal is not only to learn PySpark syntax, but to understand how Spark and Delta Lake concepts fit into real-world data engineering pipelines.

**Concept → Hands-on Practice → Real-world Scenario → Production Consideration**

## 📈 Next Steps

After the 20-day foundation:

- Productionize the Day 20 project
- Strengthen Azure Data Factory and ADLS implementation
- Advanced Spark and Delta Lake
- Structured Streaming
- Data warehousing and dimensional modelling
- Azure security and governance
- CI/CD for data pipelines
- Architecture case studies
- Data Engineering interview preparation

---

**20 Days of PySpark Data Engineering — Learn → Practice → Build → Document → Grow**
