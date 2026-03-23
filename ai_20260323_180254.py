 Here's a simple example of SQL query optimization using EXPLAIN and JOIN rewriting techniques:

```sql
-- Original query
SELECT A.id, B.name, C.description
FROM table_a AS A
JOIN table_b AS B ON A.ref_id = B.id
JOIN table_c AS C ON A.another_ref_id = C.id;

-- Optimized query with subquery and index usage (for simplicity)
SELECT A.id, B.name, C.description
FROM table_a AS A
JOIN table_b AS B ON A.ref_id = B.id
JOIN (
    SELECT * FROM table_c WHERE id IN (SELECT another_ref_id FROM table_a)
) AS C ON true;

-- Query explanation before and after optimization
EXPLAIN SELECT ...; -- Original query
EXPLAIN SELECT ...; -- Optimized query
```