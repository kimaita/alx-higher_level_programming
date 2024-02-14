-- list all genres not linked to the show Dexter
WITH dexter_gen AS(
    SELECT gen.id
    FROM
        tv_genres gen
        JOIN tv_show_genres show_gen ON gen.id = show_gen.genre_id
        JOIN tv_shows ON show_gen.show_id = tv_shows.id
        AND tv_shows.title = 'Dexter'
)
SELECT name
FROM tv_genres
WHERE id NOT IN 
    (SELECT id FROM dexter_gen)
ORDER BY
    name;
