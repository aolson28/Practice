SELECT capital
FROM countries
WHERE
  continent LIKE 'Afr%'
  AND
  country LIKE 'E%'
GROUP BY capital
ORDER BY capital ASC
LIMIT 3;

--P table
--R column capital where continent is 'Africa' or 'Afrika' and country starts with 'E'
--P ORDER BY capital, limi t 3, and use where statements
