-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- format: tv_shows.title - rating sum
SELECT
    tv.title,
    SUM(show_rate.rate) AS rating
FROM
    tv_shows tv
    LEFT JOIN tv_show_ratings show_rate ON tv.id = show_rate.show_id
GROUP BY
    title
ORDER BY
    rating DESC;
