/*Query the average population for all cities in CITY, rounded down to the nearest integer.*/

SELECT FLOOR(AVG(Population)) AS avg_population
FROM CITY;