import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = "database/users.db"


def create_user_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        email TEXT UNIQUE,

        password TEXT

    )

    """)

    connection.commit()

    connection.close()


def add_user(username, email, password):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    hashed_password = generate_password_hash(password)

    cursor.execute(

        "INSERT INTO users(username,email,password) VALUES(?,?,?)",

        (username, email, hashed_password)

    )

    connection.commit()

    connection.close()


def get_user(email):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(

        "SELECT * FROM users WHERE email=?",

        (email,)

    )

    user = cursor.fetchone()

    connection.close()

    return user


def validate_user(email, password):

    user = get_user(email)

    if user:

        if check_password_hash(user[3], password):

            return user

    return None