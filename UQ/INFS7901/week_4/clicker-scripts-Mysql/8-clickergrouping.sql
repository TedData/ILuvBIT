drop table Arc;

create table Arc(
x integer,
y integer
);

insert into Arc values(1,2);
insert into Arc values(1,2);
insert into Arc values(2,3);
insert into Arc values(3,4);
insert into Arc values(3,4);
insert into Arc values(4,1);
insert into Arc values(4,1);
insert into Arc values(4,1);
insert into Arc values(4,2);

SELECT a1.x, a2.y, COUNT(*) 
FROM Arc a1, Arc a2
WHERE a1.y = a2.x
GROUP BY a1.x, a2.y;