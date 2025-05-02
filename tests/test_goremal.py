import pytest


@db_connector
def test(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)


sqlQuery = "select " \
    "GOREMAL_PIDM, " \
    "Count(*) count " \
    "FROM GENERAL.GOREMAL " \
    "WHERE GOREMAL_EMAL_CODE = 'REC1' " \
    "AND GOREMAL_STATUS_IND = 'A' " \
    "AND GOREMAL_PREFERRED_IND = 'Y' " \
    "GROUP BY GOREMAL_PIDM " \
    "HAVING Count(GOREMAL_PIDM) > 1"

test(sqlQuery)


    