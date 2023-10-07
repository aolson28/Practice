Select s, UPPER(s) AS res
FROM makeuppercase;

--P string
--R string but uppercase
--E 'test' -> 'TEST'
--P use UPPER()
--# write your SQL statement here: you are given a table 'makeuppercase' with column 's', return a table with column 's' and your result in a column named 'res'.