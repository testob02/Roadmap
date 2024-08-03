SELECT title, release_year
from movies
where studio = "marvel studios";

SELECT title
from movies
where title like "%avenger%";

SELECT release_year
from movies
where title = "The Godfather";

SELECT distinct studio
from movies
where industry = "Bollywood" and studio != ""; 
