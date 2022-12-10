SELECT title FROM movies, people, stars
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = "Johnny Depp"
AND title IN (SELECT title FROM movies, people, stars
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = "Helena Bonham Carter")