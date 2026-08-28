import sqlite3

conn = sqlite3.connect("certificates.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO certificates
(certificate_id, student_name, course, institution, issue_date, status)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "CERT001",
    "Mohan",
    "Python Programming",
    "ABC College",
    "2026-08-27",
    "Valid"
))

conn.commit()
conn.close()

print("Certificate added successfully!")