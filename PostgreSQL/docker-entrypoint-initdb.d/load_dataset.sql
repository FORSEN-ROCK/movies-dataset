/* At first load users into user*/
COPY user
FROM './../../dataset/users.csv'
DELIMITER ','
CSV HEADER;

/* Next load movies */
COPY movie
FROM './../../dataset/movies.csv'
DELIMITER ','
CSV HEADER;

/* Now losd rating */
COPY rating
FROM './../../dataset/ratings.csv'
DELIMITER ','
CSV HEADER;

COPY movie_link
FROM './../../dataset/links.csv'
DELIMITER ','
CSV HEADER;

COPY tag
FROM './../../dataset/tags.csv'
DELIMITER ','
CSV HEADER;