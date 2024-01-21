drop table if exists Scores;
create table Scores(
 Team varchar(20),
 Day	varchar(10),
 Opponent varchar(20),
 Runs integer);


insert into Scores values('Dragons','Sun','Swallows',4);
insert into Scores values('Tigers','Sun','Bay Stars',9);
insert into Scores values('Carp','Sun',NULL,NULL);
insert into Scores values('Swallows','Sun','Dragons',7);
insert into Scores values('Bay Stars','Sun','Tigers',2);
insert into Scores values('Giants','Sun',NULL,NULL);
insert into Scores values('Dragons','Mon','Carp',NULL);
insert into Scores values('Tigers','Mon',NULL,NULL);
insert into Scores values('Carp','Mon','Dragons',NULL);
insert into Scores values('Swallows','Mon','Giants',0);
insert into Scores values('Bay Stars','Mon',NULL,NULL);
insert into Scores values('Giants','Mon','Swallows',5);
SELECT COUNT(*),COUNT(Runs)
FROM Scores 
Where Team = 'Carp';