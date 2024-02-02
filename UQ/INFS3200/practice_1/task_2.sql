/*Change Full Replication code*/

UPDATE USER1_HF_FULL_S4663588.ATHLETE1_REPLICA1
SET ATHLETE1_REPLICA1.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA1.ATHLETEID = 305;

UPDATE USER2_HF_FULL_S4663588.ATHLETE1_REPLICA2
SET ATHLETE1_REPLICA2.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA2.ATHLETEID = 305;

UPDATE USER3_HF_FULL_S4663588.ATHLETE1_REPLICA3
SET ATHLETE1_REPLICA3.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA3.ATHLETEID = 305;


/*Change Partial Replication code*/

UPDATE USER1_HF_PA_S4663588.ATHLETE1_REPLICA1
SET ATHLETE1_REPLICA1.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA1.ATHLETEID = 305;

UPDATE USER2_HF_PA_S4663588.ATHLETE1_REPLICA2
SET ATHLETE1_REPLICA2.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA2.ATHLETEID = 305;


/*Change No Replication code*/

UPDATE USER1_HF_NO_S4663588.ATHLETE1_REPLICA1
SET ATHLETE1_REPLICA1.CCODE = 'AUS'
WHERE ATHLETE1_REPLICA1.ATHLETEID = 305;
