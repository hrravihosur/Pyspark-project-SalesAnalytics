# Day 19 — Delta Lake, CDC and MERGE

Covered Delta Lake transactions, CDC operations (Insert / Update / Delete), source deduplication, Delta MERGE / UPSERT and idempotent incremental processing.

A key exercise used `customer_id` as the business key and `updated_at` with a window function to keep the latest CDC record before MERGE.

**Key takeaway:** MERGE supports idempotent designs when the business key, source deduplication and merge logic are deterministic.