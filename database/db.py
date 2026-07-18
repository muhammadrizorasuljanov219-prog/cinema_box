import sqlite3

db = sqlite3.connect("cinema.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE,
    name TEXT,
    genre TEXT,
    year TEXT,
    imdb TEXT,
    file_id TEXT
)
""")
db.commit()


def add_movie(code, name, genre, year, imdb, file_id):
    cursor.execute(
        """
        INSERT INTO movies(code, name, genre, year, imdb, file_id)
        VALUES(?, ?, ?, ?, ?, ?)
        """,
        (code, name, genre, year, imdb, file_id)
    )
    db.commit()


def get_movie(code):
    cursor.execute(
        "SELECT file_id FROM movies WHERE code=?",
        (code,)
    )
    return cursor.fetchone()
def delete_movie(code):
    cursor.execute(
        "DELETE FROM movies WHERE code=?",
        (code,)
    )
    db.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE
)
""")

db.commit()
def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    db.commit()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def movies_count():
    cursor.execute("SELECT COUNT(*) FROM movies")
    return cursor.fetchone()[0]


def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()