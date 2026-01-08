SELECT activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE('2019-07-27') - INTERVAL 29 DAY AND '2019-07-27'
-- AND activity_type IN ('open_session', 'end_session', 'scroll_down', 'send_message')
GROUP BY activity_date;