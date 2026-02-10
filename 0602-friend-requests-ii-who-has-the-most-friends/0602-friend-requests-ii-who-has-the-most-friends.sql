SELECT requester_id AS id, COUNT(requester_id) AS num
FROM (SELECT requester_id, accepter_id 
FROM RequestAccepted

UNION ALL

SELECT accepter_id AS requester_id, requester_id AS accepter_id
FROM RequestAccepted) T
GROUP BY requester_id
ORDER BY COUNT(requester_id) DESC
LIMIT 1;