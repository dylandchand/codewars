/*
Create a simple SELECT query to display student information of all ACTIVE students.

TABLE STRUCTURE:

students
Id (integer)	FirstName (text)	LastName (text)	IsActive (boolean)
*/

SELECT * FROM students WHERE isActive = 1;