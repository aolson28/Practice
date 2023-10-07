SELECT flower1, flower2 ,
CASE WHEN flower1 % 2 != flower2 % 2 THEN true ELSE false END AS res
FROM love;

--P bool
--R true or false when one of the flowers is odd number of petals and the other is even number of petals
--E 1 and 3 = false; 1 and 2 = true
--P compare modulo of both flowers
-- # write your SQL statement here: you are given a table 'love' with columns 'flower1' and 'flower2', return a table with all the columns and your result in a column named 'res'.