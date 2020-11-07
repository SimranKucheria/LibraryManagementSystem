# Library Management System

##DBMS MINI PROJECT SYNOPSIS

**PARTNER**:- Shruti Susan Mathews(111803134)

**Repository hosted at**:www.github.com/SimranKucheria/LibraryManagementSystem

**Problem Statement**
&nbsp Library Management System

**Introduction**
This is a basic Library Management System using python and SQL, It can be used in schools/colleges
to monitor the day to day requirements of the library.

**Features**
The system will have 2 modes depending on who is using it(Staff/Students)
Staff mode will only be accessible using password (Hardcoded as 17 for now)

Staff
1)Register-Books, Students, Authors, Genres(Categories as well as adding genres to books), Personal info
2)View-Students(All, Department wise), Personal info of students
3)Delete-Students, Books, Authors, Genres
4)Update/Modify-Books(Restocking, changing info), Authors, Students
5)Manage fines, enquiries and comments(Use to pay and acknowledge fines and enquiries)

Student
1)Display- Books(All, Genre wise, Author wise), Authors, Borrowed books(using Student ID), Fines(of a particular student)
2)Issue/Return/Report lost books
3)Search for books using Genre, Author, Title
4)Add enquiries/Comments

**TechStack**
Frontend used-Tkinter(Python)
Backend- Python + Mysql

**Files in repo**
MainCode-For setting up GUI menus
Create.py-Creates all tables in sql
Inventory.py-Code for all options (staff/student)
Bg.ppm-Background image for system
Schema1.jpg-Schema of database

**Installation instructions**
1)Run mysql
2)Create a database library
3) Run the foll. Instructions
USE Library;
CREATE USER ‘LibraryStaffs@localhost’ IDENTIFIED BY ‘Staffpw’; 
                GRANT ALL ON library.*  TO 'LibraryStaffs'@'localhost'
4)Run Create.py first
	Python Create.py
5)Then run MainCode.py
	Python MainCode.py

**Screenshots**
Screenshots of all functions and menus attached in ss folder

**Schema**
Refer to schema1.jpg

