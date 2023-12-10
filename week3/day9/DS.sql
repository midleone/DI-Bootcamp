-- CREATE TABLE actors (
--      id serial PRIMARY KEY,
--      last_name VARCHAR(255),
--      first_name VARCHAR(255)
-- );
INSERT INTO actors (last_name, first_name) VALUES
   ('Marc', 'Benichou'),
   ('Yoan', 'Cohen'),
   ('Lea', 'Benichou');

SELECT COUNT(*) AS actor_count FROM actors;