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
/* VALUES ("Mrs", "She is good", "2024-11-01 10:30:00" ),
       ("Miss", "She is kind", "2024-11-02 12:00:00"),
       ("Madam", "She is hardworking","2024-11-03 14:15:00"); */