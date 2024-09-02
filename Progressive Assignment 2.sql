CREATE database University_StudentManagementSystem;

Use  University_StudentManagementSystem;

Create table Students
(Students_Id INT primary key, First_name varchar (30),
last_name varchar (30), DOB date, Gender char (10),
Email varchar (30), Phone_no varchar (15) );


Create table Course
(Course_id INT primary key, Course_name varchar (30),
course_description text, Grade int); 


Create table Instructors
(Instructors_id INT primary key, First_name varchar (30),
Last_name varchar (30), Email varchar (30),
Phone_number varchar (15)); 