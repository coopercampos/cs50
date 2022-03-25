--  all movies released in 2010 and their ratings, in descending order by rating. --
SELECT
    movies.title,
    ratings.rating
FROM
    movies
    INNER JOIN ratings ON ratings.movie_id = movies.id
WHERE
    movies.year = 2010
ORDER BY
    ratings.rating DESC,
    movies.title ASC;
    