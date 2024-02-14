-- lists all genres from hbtn_0d_tvshows and the number of shows linked to each.
-- format: <TV Show genre> - <Number of shows linked to this genre>
SELECT
    gen.name AS genre,
    COUNT(show_id) AS number_of_shows
FROM
    tv_show_genres show_gen
JOIN tv_genres gen ON show_gen.genre_id = gen.id
GROUP BY
    genre
ORDER BY
    number_of_shows DESC;
