SELECT * , FLOOR(hours / 2) AS liters
FROM cycling;

--P integer
--R number of liters, rounded down where 0.5 liter per hour
--E 9.2 hrs / 2 is 4.6, rounded down is 4 liters
--P Use floor(hours / 2)


