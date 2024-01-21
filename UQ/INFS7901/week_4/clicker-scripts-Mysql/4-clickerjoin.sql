drop table if exists R;
drop table if exists S;
drop table if exists T;

create table R(
a integer,
b integer
);
create table S(
a integer,
b integer
);
create table T(
a integer,
b integer
);

insert into R values(0,0);
insert into R values(0,1);
insert into R values(1,0);
insert into R values(1,1);


insert into S values(0,0);
insert into S values(0,1);
insert into S values(1,0);
insert into S values(1,1);


insert into T values(0,0);
insert into T values(0,1);
insert into T values(1,0);
insert into T values(1,1);

SELECT  R.a, R.b, S.b, T.b
FROM R,S,T
WHERE R.b = S.a and S.b <> T.b;