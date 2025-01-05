WITH RECURSIVE CTE_HOUR AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1
    FROM CTE_HOUR
    WHERE HOUR < 23
)

SELECT 
    C.HOUR,
    COUNT(A.DATETIME) AS COUNT
FROM CTE_HOUR AS C LEFT JOIN ANIMAL_OUTS AS A ON C.HOUR = HOUR(A.DATETIME)
GROUP BY HOUR