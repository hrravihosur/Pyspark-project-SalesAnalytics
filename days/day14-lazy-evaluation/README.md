# Day 14 — Lazy Evaluation

Spark transformations are lazy: Spark builds a logical execution plan and generally executes work only when an action requires a result.

**Key takeaway:** Understanding laziness helps explain why transformation chains can be optimized before execution.
