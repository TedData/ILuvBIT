drop table if exists R;
drop table if exists S;
create table R(
A integer,
B integer);
create table S(
B integer,
C integer,
D integer);
insert into R values(1,2);
insert into R values(3,4);
insert into R values(5,6);
insert into S values(2,4,6);
insert into S values(4,6,8);
insert into S values(4,7,9);

SELECT R.A, R.B, S.B, S.C, S.D 
FROM R left OUTER JOIN S
ON (R.A > S.B and R.B   = S.C)
union 
SELECT R.A, R.B, S.B, S.C, S.D 
FROM R right OUTER JOIN S
ON (R.A > S.B and R.B   = S.C);