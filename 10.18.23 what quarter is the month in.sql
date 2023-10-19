SELECT month, 
CAST(FLOOR((month + 2)/3) AS int) AS res
FROM quarterof;

--P table
--R table with month and the quarter of the year
--E 5 -> 2
--P int representing quarter