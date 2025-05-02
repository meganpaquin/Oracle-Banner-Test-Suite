import pytest
from settings.connections import db_connector

@db_connector
def test(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

sqlQuery = "select " \
    "GOREMAL_PIDM, " \
    "Count(*) count " \
    "FROM GENERAL.GOREMAL " \
    "WHERE GOREMAL_EMAL_CODE = 'REC1' " \
    "AND GOREMAL_STATUS_IND = 'A' " \
    "AND GOREMAL_PREFERRED_IND = 'Y' " \
    "GROUP BY GOREMAL_PIDM " \
    "HAVING Count(GOREMAL_PIDM) > 1"

cursor = test(sqlQuery)

def test_multiple_emails():
    assert len(cursor) == 0

