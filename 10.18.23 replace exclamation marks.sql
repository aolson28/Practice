SELECT s, REPLACE(s,'!','') AS res
FROM removeexclamationmarks;

--P table
--R table with strings with exclamation marks removed
--E 'You're doing great!' = 'You're doing great'
--P can just use REPLACE() function