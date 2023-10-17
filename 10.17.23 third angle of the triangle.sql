SELECT a, b , (180 - a - b) AS res
FROM otherangle;

--P table with int column as res
--R table with a, b, and res column that shows the third angle of the triangle (sum of triangle angles is always 180)
--E 15, 90 -> 15, 90, 75
--P can use 180 - a- b to give the 3rd column AS res