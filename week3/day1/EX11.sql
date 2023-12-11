CREATE TABLE items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255),
    price INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
INSERT INTO items (item_id, item_name, price) VALUES
(1, 'Small Desk', 100),
(2, 'Large Desk', 300),
(3, 'Fan', 80);
INSERT INTO customers (customer_id, first_name, last_name) VALUES
(1, 'Greg', 'Jones'),
(2, 'Sandra', 'Jones'),
(3, 'Scott', 'Scott'),
(4, 'Trevor', 'Green');

SELECT * FROM items;
SELECT * FROM items WHERE price <= 300;
SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith';

SELECT * FROM customers WHERE last_name = 'Jones';

SELECT * FROM customers WHERE first_name != 'Scott';



-- SELECT name ||''|| description as namedesv FROM products

-- SELECT FROM products не использовать в проде
-- SELECT name FROM products
-- SELECT name, id FROM products
-- INSERT INTO products (description, name,price)
-- VALUES ('bla bla bla','ipad14', 900),
-- ('bbhb','iwach',600),
-- ('gd', 'icar', 10000)



-- CREATE TABLE products (
-- 	id serial PRIMARY KEY,
-- 	name varchar(255) NOT NULL,
-- 	password varchar(50) NOT NULL,
-- 	description varchar(100),
-- 	price integer NOT NULL
	
-- )


-- CREATE TABLE myuserstablee (
--     id serial PRIMARY KEY,
-- 	email varchar(255) UNIQUE NOT NULL,
-- 	password varchar(1000),
-- 	created_date timestamp default now()
-- )




-- CREATE TABLE accounts (
-- 	user_id serial PRIMARY KEY,
-- 	username varchar(50) UNIQUE NOT NULL,
-- 	password varchar(50) NOT NULL,
-- 	email varchar(255) UNIQUE NOT NULL,
-- 	create_on timestamp not null default now(),
-- 	last_login timestamp
-- )

-- UNIQUE
-- NOT NULL
-- PRIMARY KEY
-- FOREIGN KEY