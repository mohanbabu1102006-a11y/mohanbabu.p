import sqlite3


DATABASE_NAME = "certificates.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            certificate_id TEXT UNIQUE NOT NULL,
            student_name TEXT NOT NULL,
            course TEXT NOT NULL,
            institution TEXT NOT NULL,
            issue_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_certificate(
    certificate_id,
    student_name,
    course,
    institution,
    issue_date
):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO certificates
            (
                certificate_id,
                student_name,
                course,
                institution,
                issue_date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            certificate_id,
            student_name,
            course,
            institution,
            issue_date,
            "Valid"
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def verify_certificate(certificate_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            certificate_id,
            student_name,
            course,
            institution,
            issue_date,
            status
        FROM certificates
        WHERE certificate_id = ?
    """, (certificate_id,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_all_certificates():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            certificate_id,
            student_name,
            course,
            institution,
            issue_date,
            status
        FROM certificates
        ORDER BY id DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results