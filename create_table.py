import sqlite3

conn = sqlite3.connect('otroci.db')
c = conn.cursor()

c.execute("CREATE TABLE users (id int, email text, zprava1 int, zprava2 int, zprava3 int)")

conn.commit()

conn.close()
