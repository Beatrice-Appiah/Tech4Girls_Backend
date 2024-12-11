-- 
-- An sql script for setting up and populating a database.

-- Creates a database Tech4Girls_DB
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

-- Shows databses
SHOW DATABASES;

-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create a table 'Users'
CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert values into Users table
INSERT INTO Users (username, email)
VALUES ("ama", "ama@example.com"),
       ("Abena", "abena@example.com"),
       ("adjoa", "adjoa@example.com");

-- Selects all columns and rows from the table Users and displays it
SELECT * FROM Users;