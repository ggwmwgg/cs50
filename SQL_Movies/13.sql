SELECT DISTINCT(name) FROM people
JOIN movies ON stars.movie_id = movies.id
JOIN stars ON people.id = stars.person_id
WHERE movies.title IN(
SELECT DISTINCT(movies.title) FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE name = "Kevin Bacon" and birth = 1958) AND name != "Kevin Bacon";