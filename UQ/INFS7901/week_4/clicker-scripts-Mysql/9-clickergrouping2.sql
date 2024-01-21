drop table if exists Flight;

create table Flight(
origin char(5),
dest char(5)
);

insert into Flight values('SFO','YVR');
insert into Flight values('SFO','YVR');
insert into Flight values('YVR','SEA');
insert into Flight values('SEA','PIT');
insert into Flight values('SEA','PIT');
insert into Flight values('PIT','SFO');
insert into Flight values('PIT','SFO');
insert into Flight values('PIT','SFO');
insert into Flight values('PIT','YVR');

SELECT f1.origin, f2.dest, COUNT(*) 
FROM Flight f1, Flight f2
WHERE f1.dest = f2.origin
GROUP BY f1.origin, f2.dest;
