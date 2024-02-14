--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tshow.title, show_gen.genre_id
FROM tv_shows tshow INNER JOIN tv_show_genres show_gen ON tshow.id = show_gen.show_id
ORDER BY title, genre_id;