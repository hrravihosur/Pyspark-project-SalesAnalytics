-- Day 20 — Example Gold SQL
-- Adapt table names to the target Databricks catalog/schema.

-- Sales by country
SELECT
    country,
    SUM(amount) AS total_sales,
    COUNT(order_id) AS order_count
FROM enriched_sales
GROUP BY country
ORDER BY total_sales DESC;

-- Sales by category
SELECT
    category,
    SUM(amount) AS total_sales,
    COUNT(order_id) AS order_count
FROM enriched_sales
GROUP BY category
ORDER BY total_sales DESC;

-- Customer sales summary
SELECT
    customer_id,
    customer_name,
    country,
    status,
    SUM(amount) AS total_sales,
    COUNT(order_id) AS order_count
FROM enriched_sales
GROUP BY customer_id, customer_name, country, status
ORDER BY total_sales DESC;

-- Reconciliation
SELECT SUM(amount) AS total_sales
FROM enriched_sales;
-- Expected: 745000
