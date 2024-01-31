/*If tables with the name 'Branch' and 'Customer' already exist, then delete them.*/
drop table if exists Stuff;
drop table if exists Car;
drop table if exists Customer;
drop table if exists Branch;
drop trigger if exists tr;





/*Create the 'branch' table*/
CREATE TABLE Branch
( B_ID varchar(255), /*Username is of type varchar (variable character field) and has a length of 255 (can hold 0 - 255 characters)*/
Location varchar(255),
Phone_number varchar(255),
PRIMARY KEY (B_ID) /*Each user can be identified with their username*/
);

/* Branch data*/
Insert into Branch VALUES ('X1', 'Brisbane', '(07) 3346 5700');
Insert into Branch VALUES ('X2', 'Auckland', '(021) 9978 9400');
Insert into Branch VALUES ('X3', 'Sydney', '(02) 9250 6111');
Insert into Branch VALUES ('X4', 'Melbourne', '(03) 8620 3222');
Insert into Branch VALUES ('X5', 'Canberra', '(02) 6245 3100');


/*Create the 'customer' table*/
CREATE TABLE Customer
( D_number int(255) primary key auto_increment, /*Username is of type varchar (variable character field) and has a length of 255 (can hold 0 - 255 characters)*/
Name varchar(255),
Phone_No varchar(255),
Email varchar(255),
V_ID varchar(255)
);

/*Add customer to database*/
Insert into Customer(Name, Phone_No, Email, V_ID) VALUES ('Victoria Beckham', '04000001', '04000001@gmail.com', 'X113');
insert into Customer(Name, Phone_No, Email, V_ID) VALUES ('Britney Spears', '04000002', '04000002@gmail.com', 'X214');
insert into Customer(Name, Phone_No, Email, V_ID) VALUES ('Brad Pitt', '+614000003', '04000003@gmail.com', 'X311');
insert into Customer(Name, Phone_No, Email, V_ID) VALUES ('Nicole Kidman', '04000004', '04000004@gmail.com', 'X415');
insert into Customer(Name, Phone_No, Email, V_ID) VALUES ('Angelina Jolie', '+614000005', '04000005@gmail.com', 'X512');

/*Create the Car table*/
CREATE TABLE Car
( V_ID varchar(255),
B_ID varchar(255),
Model varchar(255),
Kilometers varchar(255),
Price int(255),
C_Year int(255),
Accident varchar(255),
Car_brand varchar(255),
PRIMARY KEY (V_ID),
FOREIGN KEY (B_ID) references Branch(B_ID) ON DELETE CASCADE
);

/*Add Car info to database*/
Insert into Car VALUES ('X101', 'X1', 'AUTO','50000+','6000','2009','N','HONDA');
Insert into Car VALUES ('X102', 'X1', 'HAND','70000+','3000','2010','Y','lamborghini');
Insert into Car VALUES ('X201', 'X2', 'AUTO','90000+','7000','2012','N','lamborghini');
Insert into Car VALUES ('X202', 'X2', 'HAND','150000+','15000','2020','N','BMW');
Insert into Car VALUES ('X301', 'X3', 'AUTO','30000+','22000','2018','N','lamborghini');
Insert into Car VALUES ('X302', 'X3', 'AUTO','500000+','10000','2019','N','BMW');
Insert into Car VALUES ('X401', 'X4', 'AUTO','600000+','30000','2012','N','lamborghini');
Insert into Car VALUES ('X402', 'X4', 'AUTO','900000+','60000','2017','N','lamborghini');
Insert into Car VALUES ('X501', 'X5', 'HAND','150000+','150000','2021','Y','lamborghini');
Insert into Car VALUES ('X502', 'X5', 'AUTO','3000000+','2000','2019','N','lamborghini');



/*Create the 'stuff' table*/
CREATE TABLE Stuff
(S_ID varchar(255),
B_ID varchar(255),
Location varchar(255),
name varchar(255),
email varchar(255),
PRIMARY KEY (S_ID),
FOREIGN KEY (B_ID) references Branch(B_ID) ON DELETE CASCADE
);

/*Add users and blogs to database*/

Insert into Stuff VALUES ('X1-1', 'X1','Brisbane','Jane', 'Jane@gmail.com');
Insert into Stuff VALUES ('X1-2', 'X1','Brisbane','Jake', 'Jake@gmail.com');
Insert into Stuff VALUES ('X2-1', 'X2', 'Auckland','Tom', 'Tom@gmail.com');
Insert into Stuff VALUES ('X2-2', 'X2', 'Auckland','Tim', 'Tim@gmail.com');
Insert into Stuff VALUES ('X3-1', 'X3', 'Sydney','Tony', 'Tony@gmail.com');
Insert into Stuff VALUES ('X3-2', 'X3', 'Sydney','Alan', 'Alan@gmail.com');
Insert into Stuff VALUES ('X4-1', 'X4', 'Melbourne','Ben', 'Ben@gmail.com');
Insert into Stuff VALUES ('X4-2', 'X4', 'Melbourne','Kai', 'Kai@gmail.com');
Insert into Stuff VALUES ('X5-1', 'X5', 'Canberra','Joson', 'Joson@gmail.com');
Insert into Stuff VALUES ('X5-2', 'X5','Canberra','Marry', 'Marry@gmail.com');



create trigger tr 
AFTER INSERT on Customer FOR EACH ROW
delete from Car WHERE V_ID=new.V_ID;


