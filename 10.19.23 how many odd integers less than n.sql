SELECT n,
CASE
  WHEN n %2 = 0 THEN n/2
  ELSE (n - 1)/2 
END
AS res
FROM oddcount;

--P table
--R table with int as res of count of odd numbers < n
--E 7 -> 3
--P could use floor(n/2) or just n/2 AS res