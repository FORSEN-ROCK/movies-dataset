CREATE TABLE IF NOT EXISTS movie (
	id INT PRIMARY KEY,
	titel VARCHAR(100) UNIQUE,
	genres VARCHAR(100)
)