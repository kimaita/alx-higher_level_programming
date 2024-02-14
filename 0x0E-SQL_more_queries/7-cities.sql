-- creates the table cities in hbtn_0d_usa on the MySQL server.
-- cities:
--      id: INT unique, auto generated, non-null  and is a primary key
--      state_id: INT, non-null and is a FOREIGN KEY referencing the states 
--      name: VARCHAR(256) non-null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
)
