# Day 20 — Architecture Notes

## Layers

### Landing
Raw files copied from source systems by the orchestration layer.

### Bronze
Delta representation of source data with minimal transformation and ingestion metadata. It provides a durable raw layer for replay and auditability.

### Silver
Validated and conformed data. Customer CDC is deduplicated using `customer_id` and latest `updated_at`, then applied using Delta MERGE. Orders are standardized and validated. Customer and order data are integrated with a LEFT JOIN.

### Gold
Business-ready datasets for analytics: country sales, category sales and customer sales summary.

## Orchestration

Azure Data Factory is responsible for scheduling, parameters, dependencies, retries and triggering Databricks workloads. Databricks/PySpark performs distributed transformations, Delta operations and aggregations.

## Production checklist

- Source-to-target record counts
- Null and domain validation
- Duplicate-key checks
- Reconciliation of business totals
- Quarantine/rejected-record handling
- Incremental/CDC processing
- Idempotent design
- Partition strategy
- Small-file management
- Monitoring and alerting
- Environment-specific configuration
- Security and secrets management
