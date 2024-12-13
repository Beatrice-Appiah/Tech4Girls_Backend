-- 
-- This script is to show how many-to-many realtionships can be created between tables

USE Tech4Girls_DB;
-- Creates a table 'Courses'
CREATE TABLE IF NOT EXISTS Courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL
);

-- Creates a table 'User_Courses'
CREATE TABLE IF NOT EXISTS User_Courses(
    user_id INT ,
    course_id INT,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(course_id) REFERENCES Courses(id)  
);
SHOW TABLES;

-- Inserts values into Courses table (assuming Users table already exists)
INSERT INTO Courses (course_name)
VALUES ('Web Programming and Design Fundamentals'),
       ('AI Learning with Python'),
       ('C++ for Beginners');
SELECT * FROM Courses;
          
-- Sample User Enrollments
INSERT INTO User_Courses (user_id, course_id)
VALUES 
       (1, 1),  -- User 1 enrolled in Web Programming and Design Fundamentals
       (1, 2),  -- User 1 enrolled in AI Learning with Python
       (2, 1),  -- User 2 enrolled in Web Programming and Design Fundamentals
       (3, 3);  -- User 3 enrolled in C++ for Beginners

SELECT * FROM User_Courses;