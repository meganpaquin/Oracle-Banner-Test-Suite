import os
from pathlib import Path
from settings.connections import db_connector

@db_connector
def test(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

sqlQuery = Path("sql/goremalMultipleRec1Emails.sql").read_text()
cursor = test(sqlQuery)

def test_multiple_emails():
    assert len(cursor) == 0

