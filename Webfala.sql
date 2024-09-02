CREATE database Webfala;

Use Webfala;
Create table DS 
(student_id Varchar (10) Primary Key, Age INT, 
 student_name VARCHAR(50), State_Origin VARCHAR (50), 
 LG VARCHAR(50), Skin_Type varchar (30))
 ;
 
 Create table SD 
 (student_id Varchar (10) Primary Key, Age INT, 
 student_name VARCHAR(50), State_Origin VARCHAR (50), 
 LG VARCHAR(50), Skin_Type varchar (30))
 ;
 
 Create table CS
 (student_id Varchar (10) Primary key, Age INT, 
 student_name VARCHAR(50), State_Origin VARCHAR (50), 
 LG VARCHAR(50), Skin_Type varchar (30))
 ;
 
INSERT INTO DS (student_id, Age, student_name, State_Origin, LG, Skin_type)
VALUES
('1DS', 25, 'John Doe', 'Kwara', 'ASA', 'Fair'),
('2DS', 30, 'Jane Smith', 'OYO', 'Akinyele', 'light'),
('3DS', 27, 'Alice Johnson', 'Kwara', 'Kwara', 'Brown'),
('4DS', 35, 'Bob Brown', 'Osun', 'Ayedire', 'Very_Fair'),
('5DS', 45, 'Charlie Davis', 'Kwara', 'Edu', 'Black')
;

INSERT INTO SD (student_id, Age, student_name, State_Origin, LG, Skin_type)
VALUES
('1UD', 23, 'Naheemah Muhammed', 'Kwara', 'ASA', 'Very Fair'),
('2DR', 31, 'Adejare Musa', 'Kwara', 'Offa', 'light'),
('3ES', 25, 'Ayodele Fazia', 'Osun', 'Iremide', 'Brown'),
('4UW', 53, 'Ifeoluwa Ayoola', 'Osun', 'Ayedire', 'Very_Fair'),
('5QS', 47, 'Adisa Ganiu', 'Kwara', 'Asa', 'Black')
;

INSERT INTO CS (student_id, Age, student_name, State_Origin, LG, Skin_type)
VALUES
('1CU', 53, 'Alayo Abdulazeez', 'Oyo', 'Afijio', 'Very Fair'),
('2GC', 42, 'Ayomi Nifemi', 'Kwara', 'Ilorin west', 'light'),
('3IC', 19, 'Bashirat Musa', 'Kwara', 'Offa', 'Black'),
('4PO', 50, 'McAdam Mariam', 'Kwara', 'Ilorin North', 'Very_Fair'),
('5FX', 45, 'Babalola Kafila', 'Kwara', 'Asa', 'Black')
;

select * 
From DS
Join CS 
Join SD; -- This is called union join

Select * 
From DS
join SD on DS.State_Origin = CS.State_Origin;

