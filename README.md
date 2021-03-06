# Library Management System

## DBMS MINI PROJECT SYNOPSIS

**PARTNER**:- Shruti Susan Mathews(111803134)

**Repository hosted at** : www.github.com/SimranKucheria/LibraryManagementSystem

### Problem Statement </br>
 Library Management System

 </br>
 
### Introduction  </br>
This is a basic Library Management System using python and SQL.</br>
It can be used in schools/colleges to monitor the day to day requirements of the library.

 </br>
 
### Features</br>
The system will have 2 modes depending on who is using it(Staff/Students) </br>
Staff mode will only be accessible using password (Hardcoded as 17 for now)

</br>

##### Staff </br>
1)Register-Books, Students, Authors, Genres(Categories as well as adding genres to books), Personal info </br>
2)View-Students(All, Department wise), Personal info of students </br>
3)Delete-Students, Books, Authors, Genres </br>
4)Update/Modify-Books(Restocking, changing info), Authors, Students </br>
5)Manage fines, enquiries and comments(Use to pay and acknowledge fines and enquiries) </br>

</br>

##### Student </br>
1)Display- Books(All, Genre wise, Author wise), Authors, Borrowed books(using Student ID), Fines(of a particular student) </br>
2)Issue/Return/Report lost books </br>
3)Search for books using Genre, Author, Title </br>
4)Add enquiries/Comments </br>

### TechStack </br>
Frontend used-Tkinter(Python) </br>
Backend- Python + Mysql
 
</br>

### Files in repo </br>
MainCode-For setting up GUI menus </br>
Create.py-Creates all tables in sql </br>
Inventory.py-Code for all options (staff/student) </br>
Bg.ppm-Background image for system </br>
Schema1.jpg-Schema of database </br>

</br>

### Installation instructions </br>
1)Run mysql </br>
2)Create a database library </br>
3) Run the foll. Instructions </br>
	>USE Library; </br>
	>CREATE USER ‘LibraryStaffs@localhost’ IDENTIFIED BY ‘Staffpw’; </br>
        >GRANT ALL ON library.*  TO 'LibraryStaffs'@'localhost' </br>
4)Run Create.py first </br>
	>Python Create.py </br>
5)Then run MainCode.py </br>
	>Python MainCode.py </br>

</br>

### Screenshots </br>
Screenshots of all functions and menus attached in ss folder

</br>

### Schema </br>
Refer to schema1.jpg

