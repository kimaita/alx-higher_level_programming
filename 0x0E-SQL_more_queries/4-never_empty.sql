-- creates the table id_not_null in the provided db on the server with:
-- id INT default 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1, 
    name VARCHAR(256)
)
