SELECT SUM(SCORE) AS SCORE, HE.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_EMPLOYEES AS HE JOIN HR_GRADE AS HG ON HE.EMP_NO = HG.EMP_NO JOIN HR_DEPARTMENT AS HD ON HE.DEPT_ID = HD.DEPT_ID
GROUP BY HE.EMP_NO
ORDER BY SCORE DESC
LIMIT 1