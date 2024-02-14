-- lists all shows contained in the database hbtn_0d_tvshows.
-- format: tv_shows.title - tv_show_genres.genre_id
SELECT
    tshow.title,
    show_gen.genre_id
FROM
    tv_shows tshow
LEFT JOIN tv_show_genres show_gen ON tshow.id = show_gen.show_id
ORDER BY
    title,
    genre_id;
    