SELECT title,name
from movies m
join languages l
on m.language_id = l.language_id;

SELECT title
from movies m
left join languages l
on m.language_id = l.language_id
where name='telugu';

SELECT l.name,COUNT(m.movie_id) as cnt
from movies m
left join languages l
on m.language_id = l.language_id
group by l.name
order by cnt desc

