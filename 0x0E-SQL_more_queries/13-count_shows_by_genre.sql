-- Lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each
-- in MySQL server
SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
