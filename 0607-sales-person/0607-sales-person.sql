SELECT S.NAME
FROM  SalesPerson S 
LEFT JOIN Orders O ON S.sales_id = O.sales_id
LEFT JOIN Company C ON C.com_id = O.com_id AND C.name = 'RED'
GROUP BY S.NAME
HAVING COUNT(C.com_id) = 0;