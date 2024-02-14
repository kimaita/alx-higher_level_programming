-- lists all shows without the genre Comedy
WITH comedy_shows AS (
    SELECT
        tv.id
    FROM
        tv_shows tv
        JOIN tv_show_genres show_gen ON tv.id = show_gen.show_id
        JOIN tv_genres gen ON gen.id = show_gen.genre_id
            AND gen.name = 'Comedy'
)
SELECT title 
FROM tv_shows
WHERE id NOT IN (SELECT id FROM comedy_shows)
ORDER BY title;
