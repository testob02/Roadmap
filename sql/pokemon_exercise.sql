USE pokemon;


-- Which Pokémon has the highest Total stat?
SELECT name, Total
FROM pokemon
WHERE total = (
				SELECT MAX(total)
				FROM pokemon
				);


-- Which Pokémon has the highest HP stat?
SELECT name, HP
FROM pokemon
WHERE hp = (
				SELECT MAX(hp)
				FROM pokemon
				);
                

-- List the top 10 Pokémon with the highest Attack stats.
SELECT name, Attack
FROM pokemon
ORDER BY Attack DESC
LIMIT 10;


-- How many Pokémon belong to each Type_1?
SELECT Type_1, COUNT(Type_1) as count
FROM pokemon
GROUP BY type_1
ORDER BY count;


-- Which Type_2 is most common among Pokémon?
SELECT Type_2, COUNT(Type_2) as count
FROM pokemon
GROUP BY Type_2
ORDER BY count DESC
LIMIT 1;


-- What is the average Speed of Pokémon for each Type_1
SELECT Type_1, ROUND(AVG(Speed),2) as average_speed
FROM pokemon
GROUP BY Type_1
ORDER BY average_speed DESC;


-- Find the Pokémon with the highest Defense and the lowest Attack.
SELECT name, Defense
FROM pokemon
WHERE defense = (
				SELECT MAX(defense)
				FROM pokemon
				);
                
SELECT name, Attack
FROM pokemon
WHERE attack = (
				SELECT MIN(attack)
				FROM pokemon
				);
                

-- Which Pokémon have both Defense and Sp_Def greater than 100?
SELECT *
FROM pokemon
WHERE Defense > 100 AND Sp_Def > 100;


-- List the top 5 Pokémon with the best Attack and Sp_Atk combined.
SELECT name,(Sp_Atk + Attack) as comb_atk
FROM pokemon
ORDER BY comb_atk DESC
LIMIT 5;


-- Which Generation has the most Pokémon?
SELECT generation, COUNT(generation) as count
FROM pokemon
GROUP BY generation
ORDER BY count DESC
LIMIT 1;


-- What is the average Total stat of Pokémon in each Generation?
SELECT generation, ROUND(AVG(Total),2) AS average_stats
FROM pokemon
GROUP BY generation
ORDER BY average_stats DESC;


-- How does the average HP vary across Generations?
SELECT generation, ROUND(AVG(hp),2) as avg_hp 
FROM pokemon
GROUP BY generation
ORDER BY generation;


-- Which 10 Pokémon have the highest Speed?
SELECT name, speed
FROM pokemon
ORDER BY speed DESC
LIMIT 10;


-- Find the fastest Pokémon in each Generation.
SELECT generation, name, speed
FROM pokemon p
WHERE speed = (
			SELECT MAX(speed)
            FROM pokemon
            WHERE generation = p.generation
)
ORDER BY generation;


-- List Pokémon with Speed greater than 100 and Attack greater than 100.
SELECT name
FROM pokemon
WHERE speed > 100 AND attack > 100;


-- Which Type_1 and Type_2 combination has the highest average Total stat?
SELECT type_1, type_2, ROUND(AVG(total),2) as total_avg
FROM pokemon
WHERE type_2 IS NOT NULL
GROUP BY type_1,type_2
ORDER BY total_avg DESC
LIMIT 1;


-- How many Pokémon have Type_1 as "Ground" and Type_2 as "Flying"?
SELECT *
FROM pokemon
WHERE type_1 = 'Ground' AND type_2 = 'Flying';

-- What is the average Total stat of Pokémon with dual types compared to single types?
SELECT 
CASE
	WHEN type_2 IS NULL THEN 'Single type'
    ELSE 'Dual type'
END as type_cat,
ROUND(AVG(total),2) as avg_total
FROM pokemon
GROUP BY type_cat;

-- Which Pokémon have Sp_Atk greater than Attack?
SELECT name
FROM pokemon
WHERE Sp_Atk > Attack;


-- List Pokémon with Sp_Def greater than 100 and HP greater than 100.
SELECT name
FROM pokemon
WHERE Sp_def > 100 AND HP > 100;


-- Which Generation has the highest average Sp_Atk stat?
SELECT generation, ROUND(AVG(sp_atk),2) as avg_sp_atk
FROM pokemon
GROUP BY generation
ORDER BY avg_sp_atk DESC
LIMIT 1;


-- Find the Pokémon with the highest combined Sp_Atk and Sp_Def stats.
SELECT name
FROM pokemon
WHERE (sp_atk + sp_def) = (
							SELECT MAX(sp_atk+sp_def)
                            FROM pokemon
                            );


-- How does the distribution of Type_1 change across different Generations?
SELECT generation, type_1, COUNT(*) as type_count
FROM pokemon
GROUP BY generation, type_1
ORDER BY generation, type_count DESC
					