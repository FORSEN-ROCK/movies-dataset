CREATE TABLE IF NOT EXISTS movie_link (
	id INT PRIMARY KEY,
	moviesId INT NOT NULL UNIQUE,
	imdbid INT,
	tmdbid INT
);