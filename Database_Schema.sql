drop database data;
create database data;
use data;
create table info1(name_user varchar(50),password_user varchar(50) ,email_user varchar(50) ,phone_user varchar(50) ,address_user varchar(50),uname varchar(50),uage varchar(50),uweight varchar(50),uheight varchar(50),selectbtn varchar(50),point1 int,point2 int,Resistance int,Rep int);
select * from info1;
create table sdata(ID INTEGER PRIMARY KEY AUTOINCREMENT,value1 int);
create table guest(ID INTEGER PRIMARY KEY AUTOINCREMENT,treatment int);
select * from sdata;
INSERT INTO guest (treatment)  
VALUES ("F");
drop table sdata;
drop table info1;

