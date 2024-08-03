SELECT *
from movies
order by release_year desc;

SELECT *
from movies
where release_year = 2022;

SELECT *
from movies
where release_year > 2020
order by release_year desc;

SELECT *
from movies
where release_year > 2020 and imdb_rating > 8;

SELECT *
from movies
where studio in ("marvel studios", "Hombale films");

SELECT title, release_year
from movies
where title like "%thor%"
order by release_year asc;

SELECT *
from movies
where studio != "marvel studios";
