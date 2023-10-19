SELECT 
CASE
  WHEN (a + b + c) >= (a * b * c) AND (a + b + c) >= ((a + b) * c) AND (a + b + c) >= (a * (b + c)) THEN (a + b + c)
  WHEN (a * b * c) >= (a + b + c) AND (a * b * c) >= ((a + b) * c) AND (a * b * c) >= (a * (b + c)) THEN (a * b * c)
  WHEN ((a + b) * c) >= (a * b * c) AND ((a + b) * c) >= (a * b * c) AND ((a + b) * c) >= (a * (b + c)) THEN ((a + b) * c)
  ELSE (a * (b + c))
  END AS res
FROM expression_matter;

--P table
--R table with the highest combination of expressions and parenthesis
--E 1, 2, 3 -> 9 ((1+2) * 3)
--P CASE statement. Should have used GREATEST((a + b + c), (a * b * c), ((a + b) * c), (a * (b + c)))