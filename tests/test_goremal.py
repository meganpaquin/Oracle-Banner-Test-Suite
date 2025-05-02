from pathlib import Path
from settings.connections import db_connector

@db_connector
def connect(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

sqlQuery = Path("sql/goremalMultipleRec1Emails.sql").read_text()
results = connect(sqlQuery)

def test_multiple_emails():
    assert len(results) == 0

