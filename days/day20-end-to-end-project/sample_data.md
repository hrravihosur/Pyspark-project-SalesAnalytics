# Day 20 — Sample Data

## Initial customers

| customer_id | customer_name | country | status |
|---:|---|---|---|
| 101 | Ravi Kumar | India | Active |
| 102 | John Smith | USA | Active |
| 103 | Priya Sharma | India | Active |
| 104 | David Brown | UK | Inactive |
| 105 | Anil Kumar | India | Active |
| 106 | Sarah Wilson | USA | Active |
| 107 | Kiran Rao | India | Active |
| 108 | Mike Taylor | UK | Active |

## Customer CDC

| customer_id | updated_at | operation | scenario |
|---:|---|---|---|
| 101 | 2026-09-10 08:30 | U | older update |
| 101 | 2026-09-10 09:15 | U | latest update wins |
| 103 | 2026-09-10 08:45 | U | status becomes Inactive |
| 105 | 2026-09-10 09:00 | D | customer deleted |
| 109 | 2026-09-10 09:05 | I | new customer |
| 110 | 2026-09-10 09:10 | I | new customer |
| 107 | 2026-09-10 09:20 | U | update |

## Orders

The sample contains 12 ERP orders across Electronics and Furniture with a total amount of **₹745,000**.

An intentional business scenario is included: order `1005` belongs to customer `105`, who is deleted from the current customer master by CDC. The order is retained as historical transaction data.
