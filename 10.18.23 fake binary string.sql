SELECT x, replace(replace(replace(replace(replace(replace(replace(replace(replace(x,'1','0'),'2','0'),'3','0'),'4','0'),'5','1'),'6','1'),'7','1'),'8','1'),'9','1') as res
FROM fakebin;

--P table
--R table with strings of numbers turned into binary where digits >=5 are 1 digits <5 are 0
--E '194837' -> '010101'
--P uses nested replaces. probably should use translate(x,'0123456789','0000011111')