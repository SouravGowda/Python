create database test;

use test;

create table users(
id int auto_increment primary key,
name varchar(50),
email varchar(50)
);

create  table purchase(
id int auto_increment primary key,
order_date date,
amount int,
user_id int,
foreign key (user_id) references users(id)
);

insert into users(name, email) values('yash','jdnkf@gmail.com');
insert into purchase(order_date, amount, user_id) values('2020-01-01',200,1);

select * from purchase;