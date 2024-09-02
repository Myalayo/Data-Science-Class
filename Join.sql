CREATE database Extra;

USE Extra;

CREATE TABLE classes 
(class_id INT PRIMARY KEY,
 class_name VARCHAR(50), 
 lecturer VARCHAR(50))
 ;
 
 INSERT INTO classes (class_id, class_name, lecturer)
VALUES
(1, 'Mathematics', 'Mr. Brown'),
(2, 'Science', 'Ms. Green'),
(3, 'History', 'Dr. White'),
(4, 'English', 'Mrs. Purple'),
(5, 'Geography', 'prof. Blue');

Select * 
From Classes;

CREATE TABLE students 
(student_id VARCHAR(5) PRIMARY KEY,
student_name VARCHAR(50), gender CHAR(1), class_id INT, 
foreign key (class_id) REFERENCES classes(class_id))
;

INSERT INTO students (student_id, student_name, gender, class_id)
VALUES
('1A', 'John Doe', 'M', 1),
('2B', 'Jane Smith', 'F', 2),
('3C', 'Alice Johnson', 'F', 1),
('4D', 'Bob Brown', 'M', 3),
('5E', 'Charlie Davis', 'M', 4),
('6F', 'Diana Prince', 'F', 4),
('7G', 'Eve Adams', 'F', 3),
('8H', 'Frank Castle', 'M', 3)
;

select * 
from students;

INSERT INTO students (student_id, student_name, gender)
VALUES
('11J', 'John Doe', 'M');

INSERT INTO students (student_id, student_name, gender)
VALUES
('0M', 'jack lee', 'M')
;

select *
from students;

-- SELECT students.class_id, student_name, gender, class_name
-- From students
-- JOIN classes ON students.class_id = classes.class_id;

-- Select *
-- From Students
-- left join classes on students.class_id = classes.class_id;

-- Union

select * 
From students
right join classes on students.class_id = classes.class_id;


