drop table R;
create table R(
a integer,
b integer,
c integer);
insert into R values (5,5,5);
insert into R values (3,6,3);
insert into R values (1,5,5);
insert into R values (5,5,6);
insert into R values (7,5,5);
insert into R values (3,6,5);

SELECT a, b, c 
FROM R
ORDER BY c DESC, b ASC;
