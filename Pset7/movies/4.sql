-- Selecting all the movies where the IMDb ratings are equal to 10.0
SELECT
    COUNT(movie_id)
FROM
    ratings
WHERE
    rating = 10.0;
    