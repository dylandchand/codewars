/* 

This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not. 

-- you will be given a table 'kata' with columns 'id', 'base', and 'factor'. 
-- return the 'id' and your result in a column named 'res'.

*/

SELECT id, base % factor = 0 as res FROM kata