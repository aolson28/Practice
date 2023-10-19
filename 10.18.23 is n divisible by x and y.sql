SELECT id, (n % x = 0) AND (n % y = 0) AS res
FROM kata;

--P table
--R table with id and bool result if n is divisible by x and y
--E 10, 2, 5 -> true 
--P bool statement using n % x and n% y both equaling 0. can also be written as (n % x) + (n % y) = 0, divisble means can be divided with no remainder, result is a full integer