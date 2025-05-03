from pathlib import Path
from settings.connections import db_connector
import logging

@db_connector
def connect(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

rec1Query = Path("sql/goremalMultipleRec1Emails.sql").read_text()
rec1Results = connect(rec1Query)

def test_multiple_emails():
    try:
        assert len(rec1Results) == 0
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        logging.error(rec1Results)
        raise


mnetQuery = Path("sql/goremalImproperMnetEmail.sql").read_text()
mnetResults = connect(mnetQuery)

def test_improper_MNET_email():
    try:
        assert len(mnetResults) == 0
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        logging.error(mnetResults)
        raise  