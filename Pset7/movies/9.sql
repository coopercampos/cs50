-- SELECTING ALL THE PEOPLE THAT STARRED IN MOVIES RELEASED IN 2004 ORDERED BY BIRTH YEAR --
SELECT
    DISTINCT name
FROM
    people
WHERE
    id IN (
        SELECT
            person_id
        FROM
            stars
        WHERE
            movie_id IN (
                SELECT
                    id
                FROM
                    movies
                WHERE
                    year = 2004
            )
    )
ORDER BY
    birth ASC;