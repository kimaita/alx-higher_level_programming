-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT
    tv.title
FROM
    tv_genres gen
JOIN tv_show_genres show_gen ON gen.id = show_gen.genre_id
    AND gen.name = 'Comedy'
JOIN tv_shows tv ON show_gen.show_id = tv.id
ORDER BY
    title;
