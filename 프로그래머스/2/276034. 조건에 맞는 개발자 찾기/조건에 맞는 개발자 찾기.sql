SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE FROM SKILLCODES S WHERE NAME IN ("Python")) OR SKILL_CODE & (SELECT CODE FROM SKILLCODES S WHERE NAME IN ("C#"))
ORDER BY ID;