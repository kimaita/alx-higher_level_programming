-- creates the table unique_id in the selected db on the server with:
-- id: INT, default=1, unique
-- name: VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE, 
    name VARCHAR(256)
)
