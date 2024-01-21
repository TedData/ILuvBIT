drop table if exists Scores;
Create table Scores(
Team varchar(20),
Opponent varchar(20),
RunsFor integer,
RunsAgainst integer
);

insert into Scores values('Dragons','Tigers',5,3);
insert into Scores values('Carp','Swallows',4,6);
insert into Scores values('Bay Stars','Giants',2,1);
insert into Scores values('Marines','Hawks',5,3);
insert into Scores values('Ham Fighters','Buffaloes',1,6);
insert into Scores values('Lions','Golden Eagles',8,12);
insert into Scores values('Tigers','Dragons',3,5);
insert into Scores values('Swallows','Carp',6,4);
insert into Scores values('Giants','Bay Stars',1,2);
insert into Scores values('Hawks','Marines',3,5);
insert into Scores values('Buffaloes','Ham Fighters',6,1);
insert into Scores values('Golden Eagles','Lions',12,8);

SELECT DISTINCT Team, RunsFor
     FROM Scores;

