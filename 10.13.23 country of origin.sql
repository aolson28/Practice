SELECT count(name) AS products, country
FROM products
WHERE country IN ('United States of America','Canada')
GROUP BY country
ORDER BY products DESC;

--P Table
--R Table with count of products and country
--E 123, 'United States of America'
--P count(name), WHERE country IN ('United States of America','Canada')