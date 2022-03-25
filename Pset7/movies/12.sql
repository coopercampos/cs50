-- Selecting all the movies titles that both Johnny Depp and Helena Bonham Carter starred together. --
SELECT
    title
FROM
    movies
WHERE
    id IN (
        SELECT
            movie_id
        FROM
            stars
        WHERE
            person_id = (
                SELECT
                    id
                FROM
                    people
                WHERE
                    name = "Helena Bonham Carter"
            )
            AND movie_id IN (
                SELECT
                    stars.movie_id AS movie_stars
                FROM
                    stars
                    INNER JOIN movies ON movies.id = stars.movie_id
                WHERE
                    stars.person_id = (
                        SELECT
                            id
                        FROM
                            people
                        WHERE
                            name = "Johnny Depp"
                    )
            )
    );