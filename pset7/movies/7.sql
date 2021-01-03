SELECT movies.title, ratings.rating FROM movies
JOIN ratings ON ratings.movie_id = movies.id
ORDER BY ratings.rating DESC, movies.title;
