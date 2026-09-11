# Day 20 — Customer Sales Analytics

## Objective
Build an end-to-end Azure-style data engineering pipeline that ingests CRM customers and ERP orders, processes CDC, creates conformed Silver data, and produces Power BI-ready Gold datasets.

## Architecture

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
   ├── Validation
   ├── CDC
   ├── Deduplication
   ├── MERGE
   └── Joins
   ↓
Silver Delta — Clean / Conformed
   ↓
Gold Delta — Business Ready
   ↓
Power BI
```

## Bronze

- Customer initial snapshot from CRM
- Customer CDC feed from CRM
- Orders from ERP
- Ingestion metadata: source system and ingestion timestamp
- Raw data is preserved with minimal transformation

## Silver — Customers

Customer CDC contains `I`, `U` and `D` operations. A window function partitions by `customer_id` and orders by `updated_at` descending so that only the latest change per customer is applied.

Delta MERGE then:

- Updates existing customers for `U`
- Deletes customers for `D`
- Inserts new customers for `I`

The sample produces 9 current customers after CDC is applied. Customer 101 demonstrates duplicate CDC events; the latest timestamp wins.

## Silver — Orders

Orders are standardized and validated:

- `order_date` converted to a date
- category trimmed
- required IDs checked
- positive amounts checked
- duplicate `order_id` checked

The sample contains 12 valid orders.

## Customer / Order Integration

Orders are joined to the current customer state using a **LEFT JOIN**. This deliberately preserves historical orders even when a customer has been deleted from the current customer master.

Customer 105 is deleted from the current customer state, but order 1005 for ₹60,000 remains in the transaction dataset.

## Gold

Three business datasets are created:

1. Sales by Country
2. Sales by Category
3. Customer Sales Summary

Sample results:

| Dataset | Result |
|---|---|
| Total orders | 12 |
| Total sales | ₹745,000 |
| India sales | ₹380,000 |
| USA sales | ₹230,000 |
| UK sales | ₹75,000 |
| Unmatched/deleted customer sales | ₹60,000 |
| Furniture sales | ₹390,000 |
| Electronics sales | ₹355,000 |

## Reconciliation

The transaction total remains **₹745,000** through the enriched Silver dataset and Gold aggregations. This is a key pipeline correctness check.

## Production Considerations

- Incremental processing instead of repeated full loads
- Data-quality validation and quarantine of rejected records
- Idempotent Delta MERGE processing
- Date-based partitioning where justified
- Predicate pushdown and partition pruning
- Broadcast joins only for safely small datasets
- AQE and appropriate shuffle partitioning
- Skew handling when needed
- Small-file optimization
- ADF orchestration, parameters, retries and monitoring
- Gold datasets designed for Power BI consumption
