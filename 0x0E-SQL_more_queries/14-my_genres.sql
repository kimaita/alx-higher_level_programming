-- lists all genres of the show Dexter
SELECT
    gen.name
FROM
    tv_genres gen
JOIN tv_show_genres show_gen ON gen.id = show_gen.genre_id
JOIN tv_shows ON show_gen.show_id = tv_shows.id
    AND tv_shows.title = 'Dexter'
ORDER BY
    name;
