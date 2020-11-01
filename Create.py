#Build-in Modules imported
import MySQLdb as mdb
from datetime import date
#con = mdb.connect('localhost', 'staffs', 'Shrutisusan26@', 'library')
con = mdb.connect('localhost', 'LibraryStaffs', 'Staffpw', 'library')
with con:
    cur = con.cursor()
    
    cur.execute("drop table ENQCO")
    cur.execute("drop table ENQSTUDENT")
    cur.execute("drop table FINE")
    cur.execute("drop table FINESTUDENT")
    cur.execute("drop table GENREBOOK")
    cur.execute("drop table GENRE")
    cur.execute("drop table PINFO")
    cur.execute("drop table ISSUED")
    cur.execute("drop table BOOKS")
    cur.execute("drop table AUTHOR")
    cur.execute("drop table STUDENT")
    
    cur.execute("create table STUDENT \
		(S_ID integer not null,\
		 Name varchar(20) not null,\
		 Department varchar(20) not null,\
		 primary key (S_ID))")  
    cur.execute("create table AUTHOR \
		(A_ID integer not null auto_increment,\
		 Name varchar(20) not null ,\
		 DOB date not null ,\
		 DOD date,\
		 primary key (A_ID))")    
    cur.execute("create table BOOKS \
		(B_ID integer not null auto_increment,\
	 	Title varchar(35) not null,\
	 	Price integer not null ,\
	 	Count integer not null, \
	 	A_ID integer, \
	 	primary key (B_ID),\
		foreign key (A_ID) references AUTHOR(A_ID) on delete set null)") 
    cur.execute("create table PINFO \
		(S_ID integer,\
		 City varchar(20) not null ,\
		 Phone varchar(12) not null,\
		 Email varchar(25) not null ,\
		 primary key (S_ID),\
		 foreign key (S_ID) references STUDENT(S_ID) on delete cascade)")    
    cur.execute("create table ISSUED \
		(B_ID integer,\
		 S_ID integer, \
		 Issuedate date not null,\
		 primary key(B_ID,S_ID),\
		 foreign key(B_ID) references BOOKS(B_ID) on delete cascade, \
		 foreign key(S_ID) references STUDENT(S_ID) on delete cascade)")
    cur.execute("create table GENRE \
		(G_ID integer not null ,\
		 GenreName varchar(10) not null ,\
		 primary key (G_ID))")
    cur.execute("create table GENREBOOK \
		(G_ID integer,\
		 B_ID integer, \
		 primary key (G_ID,B_ID),\
		 foreign key (B_ID) references BOOKS(B_ID) on delete cascade, \
		 foreign key (G_ID) references GENRE(G_ID) on delete cascade)")
    cur.execute("create table FINESTUDENT \
		(F_ID integer not null auto_increment,\
		 S_ID integer, \
		 primary key (F_ID,S_ID),\
		 foreign key (S_ID) references STUDENT(S_ID) on delete cascade)")
    cur.execute("create table FINE \
		(F_ID integer not null auto_increment,\
		 FineAmount integer not null,\
		 FineDate date not null,\
		 primary key(F_ID),\
		 foreign key(F_ID) references FINESTUDENT(F_ID) on delete cascade)")
    cur.execute("create table ENQSTUDENT \
		(E_ID integer not null,\
		 S_ID integer, \
		 primary key(E_ID,S_ID),\
		 foreign key(S_ID) references STUDENT(S_ID) on delete cascade)")
    cur.execute("create table ENQCO \
		(E_ID integer not null,\
		 Enqco varchar(100) not null,\
		 primary key(E_ID),\
		 foreign key(E_ID) references ENQSTUDENT(E_ID) on delete cascade)")
    
    cur.execute("Insert into STUDENT values('111803123','Rahib','Computer')")
    cur.execute("Insert into STUDENT values('111803125','Siddharth','Computer')")
    cur.execute("Insert into STUDENT values('111803126','Simran','Computer')")
    cur.execute("Insert into STUDENT values('111803132','Priya','Computer')")
    cur.execute("Insert into STUDENT values('111803134','Shruti','Computer')")
    cur.execute("Insert into STUDENT values('111803150','Jinit','Computer')")

    cur.execute("Insert into PINFO values('111803123','Jammu','123','rahemail')")
    cur.execute("Insert into PINFO values('111803125','Pune','125','sidemail')")
    cur.execute("Insert into PINFO values('111803126','Pune','126','simemail')")
    cur.execute("Insert into PINFO values('111803132','Pune','132','priemail')")
    cur.execute("Insert into PINFO values('111803134','Pune','134','shremail')")
    cur.execute("Insert into PINFO values('111803150','Mumbai','150','jinemai;')")

    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('J.K Rowling','1965-07-31',NULL)")
    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('Dan Brown','1964-06-22',NULL)")
    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('Rick Riordan','1964-06-05',NULL)")
    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('Rudyard Kipling','1865-12-30','1936-01-18')")
    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('Agatha Christie','1890-09-15','1976-01-12')")
    cur.execute("Insert into AUTHOR (Name,DOB,DOD) values('Arthur Conan Doyle','1859-05-22','1930-07-07')")

    cur.execute("Insert into BOOKS values ('1','Harry Potter 1',500,4,1)")
    cur.execute("Insert into BOOKS values ('2','Angels & Demons',550,4,2)")
    cur.execute("Insert into BOOKS values ('3','Percy Jackson',475,7,3)")
    cur.execute("Insert into BOOKS values ('4','Jungle Book',700,5,4)")
    cur.execute("Insert into BOOKS values ('5','Girl on the train',800,6,5)")
    cur.execute("Insert into BOOKS values ('6','Sherlock Holmes',570,6,6)")
    cur.execute("Insert into BOOKS values ('7','Harry Potter 2',600,8,1)")
    cur.execute("Insert into BOOKS values ('8','Da Vinci Code',450,3,2)")
    cur.execute("Insert into BOOKS values ('9','Percy Jackson 2',500,7,3)")
    cur.execute("Insert into BOOKS values ('10','Mandalay',500,8,4)")
    cur.execute("Insert into BOOKS values ('11','The ABC murders',800,6,5)")
    cur.execute("Insert into BOOKS values ('12','Sherlock Holmes 2',670,4,6)")   
   
    cur.execute("Insert into GENRE values ('1','Fantasy')")
    cur.execute("Insert into GENRE values ('2','Mystery')")
    cur.execute("Insert into GENRE values ('3','Thriller')")
    cur.execute("Insert into GENRE values ('4','History')")
    cur.execute("Insert into GENRE values ('5','Children')")

    cur.execute("Insert into GENREBOOK values ('1','1')")
    cur.execute("Insert into GENREBOOK values ('5','1')")
    cur.execute("Insert into GENREBOOK values ('1','7')")
    cur.execute("Insert into GENREBOOK values ('5','7')")
    cur.execute("Insert into GENREBOOK values ('1','2')")
    cur.execute("Insert into GENREBOOK values ('4','2')")
    cur.execute("Insert into GENREBOOK values ('1','8')")
    cur.execute("Insert into GENREBOOK values ('4','8')")
    cur.execute("Insert into GENREBOOK values ('1','3')")
    cur.execute("Insert into GENREBOOK values ('5','3')")
    cur.execute("Insert into GENREBOOK values ('1','9')")
    cur.execute("Insert into GENREBOOK values ('5','9')")
    cur.execute("Insert into GENREBOOK values ('5','4')")
    cur.execute("Insert into GENREBOOK values ('5','10')")
    cur.execute("Insert into GENREBOOK values ('2','5')")
    cur.execute("Insert into GENREBOOK values ('3','5')")
    cur.execute("Insert into GENREBOOK values ('2','11')")
    cur.execute("Insert into GENREBOOK values ('3','11')")
    cur.execute("Insert into GENREBOOK values ('2','6')")
    cur.execute("Insert into GENREBOOK values ('3','6')")
    cur.execute("Insert into GENREBOOK values ('2','12')")
    cur.execute("Insert into GENREBOOK values ('3','12')")

    cur.execute("Insert into ENQSTUDENT values ('1','111803126')")
    cur.execute("Insert into ENQCO values ('1','Hello')")
   
    cur.execute("Insert into FINESTUDENT (S_ID) values ('111803126')")
    cur.execute("Insert into FINE (FineAmount,FineDate) values (200,'2020-10-24')")

    cur.execute("Insert into ISSUED values (1,'111803126','2020-10-23')")
    
