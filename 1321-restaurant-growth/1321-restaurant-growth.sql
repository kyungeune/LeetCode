SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT visited_on, SUM(daily_amount) OVER (  -- 7일치 윈도우 누적합
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount
    FROM (SELECT visited_on, SUM(amount) AS daily_amount  -- 하루씩 묶어서 합계
            FROM Customer
            GROUP BY visited_on) daily
) seven_sum
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer
)
ORDER BY visited_on;