-- All the movie titles released on or after 2018 --
SELECT
    title
FROM
    movies
WHERE
    year >= 2018
ORDER BY
    title;
