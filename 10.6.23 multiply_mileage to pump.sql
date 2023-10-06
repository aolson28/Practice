SELECT distance_to_pump, mpg, fuel_left,
CASE WHEN mpg * fuel_left >= distance_to_pump THEN true ELSE false
END
AS res
FROM zerofuel;

--p bool
--r bool true or false if mpg * fuel_left >= distance_to_pump
--e 25 mpg * 2 fuel_left =50 => 50 distance_to_pump
--p use multiplication and case statement
--# write your SQL statement here: you are given a table 'zerofuel' with columns 'distance_to_pump', 'mpg' and 'fuel_left', return a table with all the columns and your result in a column named 'res'