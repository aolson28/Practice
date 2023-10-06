SELECT 
CASE WHEN yr % 100 != 0 THEN FLOOR(yr / 100 )+ 1 ELSE FLOOR(yr / 100 ) END AS century
FROM years;

--p integer
--r the century of the year
--e 1900 = 19th century; 1901 = 20th century
--p Use CASE and MODULO. And FLOOR (yr/100) ELSE FLOOR (yr/100)+1