SELECT id, base % factor = 0 AS res
  --CASE 
   -- WHEN base % factor = 0
  --  THEN true
  --  Else false
  --END AS res
FROM kata;

--P table with bool column res
--R table with id column and new column res with bool representing if factor is a factor of base
-- factor means that it can be multiplied with another integer to make the base number
--E 12,3 -> true
--P can use case statement or can just use the bool comparison AS res