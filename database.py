import sqlite3


DATABASE_NAME = "database/resume.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS resumes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        ats_score INTEGER

    )

    """)

    connection.commit()

    connection.close()


def save_resume(filename, ats_score):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(

        "INSERT INTO resumes(filename, ats_score) VALUES(?, ?)",

        (filename, ats_score)

    )

    connection.commit()

    connection.close()


def get_all_resumes():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(

        "SELECT * FROM resumes ORDER BY id DESC"

    )

    data = cursor.fetchall()

    connection.close()

    return data