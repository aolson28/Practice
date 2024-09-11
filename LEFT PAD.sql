--Left pad a number as a string with leading 0's 
SELECT RIGHT('000'+CAST(field AS VARCHAR(3)),3) FROM MY_TABLE
