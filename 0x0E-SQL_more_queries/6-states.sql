-- creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa).
-- id INT unique, auto generated, cant be null and is a primary key.
-- name VARCHAR(256) cant be null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id)
       );
