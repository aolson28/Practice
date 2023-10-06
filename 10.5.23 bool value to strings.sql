
SELECT bool, 
CASE WHEN bool THEN 'Yes' ELSE 'No'
END AS 'res'
FROM booltoword;
--p string "Yes" or "No"
--r Returns "Yes" for true and "No" for false
--e true = "Yes"
--p use case when bool = true then "Yes" else "No"; actually does not need "= true"
