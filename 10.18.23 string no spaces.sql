SELECT x, REPLACE(x,' ','') AS res
FROM nospace;

--P table
--R table with strings with no spaces 
--E 'You're doing great!' = 'You'redoinggreat!'
--P can replace ' ' with '' in x