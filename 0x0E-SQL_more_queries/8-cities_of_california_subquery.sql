-- lists all the cities of California in the database hbtn_0d_usa.
-- sorted by cities.id in ascending order
SELECT
    id,
    name
FROM
    cities
WHERE
    cities.state_id = (
        SELECT
            id
        FROM
            states
        WHERE
            name = 'California'
    );
    