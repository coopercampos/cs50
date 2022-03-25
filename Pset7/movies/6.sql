-- get the average rating of all the movies released in 2012 --
SELECT
    AVG(rating)
FROM
    ratings
WHERE
    movie_id in (
        SELECT
            id
        FROM
            movies
        WHERE
            year = 2012
    );