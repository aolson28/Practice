SELECT str, lower(reverse(str)) = lower(str) as res
FROM ispalindrome;

--P table
--R table with str and res which is bool of whether it is palindrome
--E test -> false dad -> true
--P bool comparison, use lower() to make case insensitive, str = reverse(str) to determine if palindrome