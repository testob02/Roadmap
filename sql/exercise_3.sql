SELECT COUNT(*) as cnt
from movies
where release_year between 2015 and 2022;

SELECT MIN(release_year) as min,
	   MAX(release_year) as max
from movies;

SELECT release_year,COUNT(release_year) as cnt
from movies
group by release_year
order by release_year desc;