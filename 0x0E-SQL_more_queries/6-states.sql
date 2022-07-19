-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE hbtn_0d_usa (id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL) ENGINE=INNODB;