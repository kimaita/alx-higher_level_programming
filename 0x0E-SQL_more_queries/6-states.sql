-- creates a database hbtn_0d_usa and its table states on the MySQL server.
-- states: 
--    id: INT, unique, auto generated, can’t be null and is a primary key
--    name: VARCHAR(256), can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
)
