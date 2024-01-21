drop table Scores;
create table Scores(
 Team varchar(20),
 Day	varchar(10),
 Opponent varchar(20),
 Runs integer);


insert into Scores values('Dragons','Sun','Swallows',4);
insert into Scores values('Tigers','Sun','Bay Stars',9);
insert into Scores values('Carp','Sun','Giants',2);
insert into Scores values('Swallows','Sun','Dragons',7);
insert into Scores values('Bay Stars','Sun','Tigers',2);
insert into Scores values('Giants','Sun','Carp',4);
insert into Scores values('Dragons','Mon','Carp',6);
insert into Scores values('Tigers','Mon','Bay Stars',5);
insert into Scores values('Carp','Mon','Dragons',3);
insert into Scores values('Swallows','Mon','Giants',0);
insert into Scores values('Bay Stars','Mon','Tigers',7);
insert into Scores values('Giants','Mon','Swallows',5);
SELECT Team, day
FROM Scores S1
WHERE Runs <= ALL
         (SELECT Runs FROM Scores S2
          WHERE S1.day = S2.day
         );
