/*Step one*/

Select distinct(AthleteID) from "USER1_VF_S4663588"."ATHLETE_V1";


/*Step two*/

Select c.BDate, c.CCode, c.SportID from "USER2_VF_S4663588"."ATHLETE_V2" c where c.CCODE = 'AUS' and c.AthleteID in (Select distinct(AthleteID) from "USER1_VF_S4663588"."ATHLETE_V1");


/*Step three*/

Select b.AthleteID, b.FName, b.SName, c.BDate, c.CCode, c.SportID from "USER1_VF_S4663588"."ATHLETE_V1" b, (Select c.AthleteID, c.BDate, c.CCode, c.SportID from "USER2_VF_S4663588"."ATHLETE_V2" c where c.CCODE = 'AUS' and c.AthleteID in (Select distinct(AthleteID) from "USER1_VF_S4663588"."ATHLETE_V1")) c where b.AthleteID = c.AthleteID;


/*inner-join*/
select b.AthleteID, b.FName, b.SName, c.BDate, c.CCode, c.SportID from "USER1_VF_S4663588"."ATHLETE_V1" b, "USER2_VF_S4663588"."ATHLETE_V2" c where b.AthleteID= c.AthleteID and c.CCODE='AUS';

