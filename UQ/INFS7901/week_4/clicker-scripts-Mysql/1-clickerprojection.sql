drop table if exists Scores;
Create table Scores(
Team1 varchar(20),
Team2 varchar(20),
Score1 integer,
Score2 integer
);

insert into Scores values('Dragons','Tigers',5,3);
insert into Scores values('Carp','Swallows',4,6);
insert into Scores values('Bay Stars','Giants',2,1);
insert into Scores values('Marines','Hawks',5,3);
insert into Scores values('Ham Fighters','Buffaloes',1,6);
insert into Scores values('Lions','Golden Eagles',8,12);

SELECT Score1, score2
     FROM Scores;

