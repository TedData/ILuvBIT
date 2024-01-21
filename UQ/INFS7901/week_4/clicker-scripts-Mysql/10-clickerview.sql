drop table if exists R;
drop view if exists V;

CREATE TABLE R(
a integer,
b integer,
c integer);

insert into R values(1,1,3);
insert into R values(1,2,3);
insert into R values(2,1,4);
insert into R values(2,3,5);
insert into R values(2,4,1);
insert into R values(3,2,4);
insert into R values(3,3,6);

CREATE VIEW V AS 
SELECT a+b AS d,c
FROM R;

SELECT d, SUM(c) FROM V
GROUP BY d
HAVING COUNT(*) <> 1;



