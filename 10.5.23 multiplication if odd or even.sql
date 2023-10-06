SELECT number,
CASE WHEN number % 2 = 0 THEN (number * 8) ELSE (number * 9)
END
AS res
FROM multiplication;

--p integer
--r number * 8 if number is even or number * 9 if number is odd
--e 3 -> 27 because 3 is odd, 6 -> 48 because 6 is even
--p use modulo 2 = 0 to determine odd or even