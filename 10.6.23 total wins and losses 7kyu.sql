SELECT name, SUM(won) AS won, SUM(lost) AS lost
FROM fighters
WHERE move_id NOT IN (1,2,3)
GROUP BY name
ORDER BY won DESC
LIMIT 6;

--P string , integer, integer
--R fighter name, sum of won, sum of loss, where move is not 'Hadoken', 'Shouoken', or 'Kikoken'
--E Fei Long, 2, 0
--P determine which IDs to filter out 
