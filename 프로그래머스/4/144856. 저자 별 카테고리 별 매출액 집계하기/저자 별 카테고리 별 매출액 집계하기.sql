SELECT B.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES * PRICE) AS TOTAL_SALES
FROM BOOK AS B JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID JOIN BOOK_SALES AS BS ON B.BOOK_ID = BS.BOOK_ID
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
GROUP BY B.AUTHOR_ID, CATEGORY
ORDER BY B.AUTHOR_ID, CATEGORY DESC