-- lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT title FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
