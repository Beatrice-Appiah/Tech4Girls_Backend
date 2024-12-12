--
-- This script is to show the buliding of relationshops betwwen tables 

USE Tech4Girls_DB;
-- Create a table 'Posts'
CREATE TABLE IF NOT EXISTS Posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR (255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
SHOW TABLES;

-- Insert values into Posts Table (one post for each user)
INSERT INTO Posts (user_id, title, content)
VALUES (1,"Determination", "It does not matter how slowly you go as long as you do not stop."),
       (2, "Honesty", "Honesty is the first chapter of the book of wisdom."),
       (3, "Patience", "Patience is bitter, but its fruit is sweet."); 

-- Selects all columns and rows from the table Posts and displays it
SELECT * FROM Posts;