-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT
    tshow.title,
    show_gen.genre_id
FROM
    tv_shows tshow
LEFT JOIN tv_show_genres show_gen ON tshow.id = show_gen.show_id
WHERE genre_id IS NULL
ORDER BY
    title,
    genre_id;
    