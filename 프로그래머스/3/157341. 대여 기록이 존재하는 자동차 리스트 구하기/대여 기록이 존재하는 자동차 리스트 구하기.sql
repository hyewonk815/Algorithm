SELECT DISTINCT(C.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR AS C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CR ON C.CAR_ID = CR.CAR_ID
WHERE (C.CAR_TYPE = '세단') AND (MONTH(CR.START_DATE) = '10')
ORDER BY C.CAR_ID DESC