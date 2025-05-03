from pathlib import Path
from settings.connections import db_connector

@db_connector
def connect(cnn, sql):
    cur = cnn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

nullQuery = Path("sql/sybistuNullCheck.sql").read_text()
nullResults = connect(nullQuery)

def test_null_data():
    assert len(nullResults) == 0
