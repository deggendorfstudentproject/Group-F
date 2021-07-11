import sqlite3
import datetime
from pprint import pprint


def _createDatabase():
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute(
        """ CREATE TABLE IF NOT EXISTS customers (
    first text,
    last text,
    sex text,
    age integer,
    vaccine text,
    state text,
    dateT date,
    time text
    )
    """
    )
    conn.commit()
    conn.close()


def _insertData(first, last, gender, age, vaccine, state, date, time):
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO customer VALUES(?,?,?,?,?,?,?,?)",
        (first, last, gender, age, vaccine, state, date, time),
    )
    conn.commit()
    conn.close()


def _showTable():
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer")
    pprint(c.fetchall())
    conn.commit()
    conn.close()


# _createDatabase()
# #_insertData(
#     "SALUMON",
#     "P",
#     "MALE",
#     27,
#     "ASTRAZENECA",
#     "BAVARIA",
#     datetime.date(2021, 7, 26),
#     "FORENOON",
# )
# _insertData(
#     "AMJAD",
#     "HAIDER",
#     "MALE",
#     26,
#     "PFIZER",
#     "BERLIN",
#     datetime.date(2021, 8, 21),
#     "AFTERNOON",
# )
_showTable()
