-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT
    gen.name,
    SUM(show_rate.rate) AS rating
FROM
    tv_genres gen
    JOIN tv_show_genres show_gen ON gen.id = show_gen.genre_id
    JOIN tv_show_ratings show_rate USING(show_id)
GROUP BY
    name
ORDER BY
    rating DESC;
