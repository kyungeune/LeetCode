SELECT (  # 내부에서 하나도 반환되지 않으면 NULL로 표시
    SELECT DISTINCT(SALARY)  # 같은 값 두개 이상인 경우 방지
    FROM EMPLOYEE
    ORDER BY SALARY DESC
    LIMIT 1 OFFSET 1  # 1개, 앞에서 하나 건너뛴
) AS SecondHighestSalary