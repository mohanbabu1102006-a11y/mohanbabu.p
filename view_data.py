import sqlite3

conn = sqlite3.connect("certificates.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM certificates")

data = cursor.fetchall()

for row in data:
    print(row)

conn.close()