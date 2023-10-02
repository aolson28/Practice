SELECT n, m,
CASE WHEN m > 0 AND n > 0 THEN (m * n)
ELSE 0
END
AS res
FROM paperwork

--p numbers--
--r number of pages when m or n are greater than 0--
--e 5 * 5 = 25, -5 * 5=0--
--p can't use absolute since both negative numbers. use case when m and n are greater than 0 -- 
