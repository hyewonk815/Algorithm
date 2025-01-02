-- 1. FROM
-- 2. 자동차 종류가 '세단' 또는 'SUV'
-- 3. 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능 확인 -> 해당 기간에 렌탈 기록이 없는 CAR_ID를 가져와야 한다 (NOT IN 사용)
-- 4. 30일 간의 대여 금액
-- 5. 대여 금액이 50만원 이상 200만원 미만인 자동차 -> HAVING은 SELECT 절에서 정의된 별칭(alias)이나 집계 함수 결과에 조건 적용 가능

SELECT
    C.CAR_ID,
    C.CAR_TYPE,
    ROUND(C.DAILY_FEE*30*(100-P.DISCOUNT_RATE)/100) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR C
JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE
WHERE
    C.CAR_TYPE IN ('SUV', '세단')
    AND C.CAR_ID NOT IN (SELECT CAR_ID
                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                         WHERE START_DATE <= '2022-11-30'
                         AND END_DATE >= '2022-11-01')
    AND P.DURATION_TYPE LIKE '30%'
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC