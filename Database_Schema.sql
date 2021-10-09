drop database data;
create database data;
use data;
create table info1(name_user varchar(50),password_user varchar(50) ,email_user varchar(50) ,phone_user varchar(50) ,address_user varchar(50),uname varchar(50),uage varchar(50),uweight varchar(50),uheight varchar(50),selectbtn varchar(50),point1 int,point2 int,Resistance int);
select * from info1;
create table sdata(ID INTEGER PRIMARY KEY AUTOINCREMENT,value1 int);
select * from sdata;
drop table sdata;
drop table info1;

