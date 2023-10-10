SELECT s, n, REPEAT(s, n) AS res
FROM repeatstr;

--P string
--R string s repeated n number of times
--E "ABC", 2 = "ABCABC"
--P use REPEAT(), SELECT * returned an unwanted id column