-- lists all shows and their linked genres in the database hbtn_0d_tvshows.
SELECT
    tv.title,
    gen.name
FROM
    tv_shows tv
LEFT JOIN tv_show_genres show_gen ON tv.id = show_gen.show_id
LEFT JOIN tv_genres gen ON show_gen.genre_id = gen.id
ORDER BY
    title, name;
