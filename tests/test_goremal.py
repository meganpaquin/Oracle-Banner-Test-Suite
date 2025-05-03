from pathlib import Path
from settings.connections import db_connector

@db_connector
def connect(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

rec1Query = Path("sql/goremalMultipleRec1Emails.sql").read_text()
rec1Results = connect(rec1Query)

def test_multiple_emails():
    assert len(rec1Results) == 0

mnetQuery = Path("sql/goremalImproperMnetEmail.sql").read_text()
mnetResults = connect(mnetQuery)

def test_improper_MNET_email():
    assert len(mnetResults) == 0