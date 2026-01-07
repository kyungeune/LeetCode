SELECT DISTINCT S.product_id, P.product_name
FROM Product P, Sales S
WHERE P.product_id = S.product_id
GROUP BY S.product_id
HAVING MIN(sale_date)>='2019-01-01' AND MAX(sale_date)<='2019-03-31'


-- SELECT DISTINCT S.product_id, P.product_name
-- FROM Product P, Sales S
-- WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31' AND P.product_id = S.product_id AND P.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date<'2019-01-01' OR sale_date>'2019-03-31')
-- GROUP BY S.product_id


-- SELECT P.product_id, P.product_name
-- FROM Product P, Sales S
-- WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31' AND P.product_id NOT IN 
-- GROUP BY P.product_id
-- HAVING COUNT(P.product_id) > 1;