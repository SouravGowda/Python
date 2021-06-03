create database dress_store;

use dress_store;

create table shirts(
shirt_type varchar(50),
quantity int
);

desc shirts;

insert into shirts(shirt_type,quantity) value("formal_shirt",12);
insert into shirts(shirt_type,quantity) value("causual_shirt",50);
insert into shirts(shirt_type,quantity) value("t_shirt",35);

select * from shirts where quantity between 10 and 35;
select * from shirts where not shirt_type='formal_shirt';

/* customer table*/
create table customers(
id int not null auto_increment,
customer_name varchar(50) not null,
email varchar(50) not null default "no email provided",
amount int,
primary key (id)
);

insert into customers( customer_name,email,amount) values ( 'sinchana','sinchu@yahoo.com', 400);

select * from customers;

select amount as  purschase from customers;

update customers set customer_name='roshan',email='dgsdgsg@gmail.com' where id=5;

delete from customers where id=6;

create database microdegree;

show databases;
use microdegree;

create table students(
student_id int not null auto_increment,
email varchar(60),
stu_fname varchar(50),
stu_lname varchar(50),
login_count int,
course_count int,
singup_month int,
primary key(student_id)
);

insert into students(email, stu_fname, stu_lname, login_count,course_count,singup_month) 
values('vsdjhsd@sffs.com','sourav','kc',10,5,15),('vsdjhswfdsd@sffs.com','sagar','v',11,6,14),
('dfcsds@sffs.com','santhosh','dsa',9,5,10),('efe@sffs.com','japan','akash',11,6,12),
('gfzshes@sffs.com','sinchana','hn',15,9,21),('sdsfds@sffs.com','chaya','lahari',11,6,9),
('efefe@sffs.com','sumanth','v',4,5,10),('sddsd@sffs.com','deefuvk','u',11,7,11),
('sfsf@sffs.com','santhu','gandu',7,4,10),('sfsff@sffs.com','karthik','v',11,8,11);

select * from students;

select concat(stu_fname,' ' ,stu_lname) as full_name, login_count from students;

select replace(stu_fname,'a','@') as fullnameat from students;

-- get all list of email , if email is longer tahn 7 character, truncate it with ...
select concat(substring(email,1,7),'...') from students;


select email, char_length(email) as email_length from students;

select reverse(email) from students;

select upper(stu_fname) as case_name from students ;

select ascii('A');

select distinct stu_fname,course_count from students order by course_count desc limit 0,1;

select stu_fname from students where stu_fname like '%na'; 
SELECT stu_fname LIKE '%' FROM students;

select  count(distinct stu_fname) from students;

select * from students;
-- select stu_fname,count(*) from students;

select count(stu_fname), singup_month from students group by singup_month order by singup_month ;

select stu_fname,email, login_count from students
where login_count= (select min(login_count) from students);

select   max(login_count), singup_month  from students group by singup_month
order by singup_month ;

select singup_month,login_count from students where singup_month=10;
select singup_month,sum(login_count) from students group by singup_month;

select singup_month,sum(login_count) as total from students group by singup_month having total>11;
