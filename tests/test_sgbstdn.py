from pathlib import Path
from settings.connections import db_connector
import logging 

@db_connector
def connect(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

nullQuery = Path("sql/sgbstdnNullCheck.sql").read_text()
nullResults = connect(nullQuery)

def test_null_data():
    try:
        assert len(nullResults) == 0
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        logging.error(nullResults)
        raise 
