SELECT s, SUBSTRING(s,2,LENGTH(s)-2) AS res
FROM removechar;

--P table
--R table with strings without first or last characters
--E 'You're doing great!' = 'ou're doing great'
--P can use substring, starting in character 2, for length(s)-2 for number of characters