import _sqlite3
conn = _sqlite3.connect('customers.db')
c = conn.cursor()
c.execute(""" CREATE TABLE customer (
first text,
last text,
sex text,
age integer,
vaccine text,
state text,
date real,
time text

)
""")