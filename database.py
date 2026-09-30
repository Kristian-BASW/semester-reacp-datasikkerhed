import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("app.db")


def connect() -> sqlite3.Connection:
    return sqlite3.connect(database_path)


def initialize_database() -> None:
    # Opretter tabel kaldet tasks med kolonnerne id (primary key), title, description
    with connect() as database:
        database.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)
    
    # Opretter tabel kaldet users med kolonnerne id (primary key), username og password
    with connect() as database:
        database.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                cprNumber TEXT NOT NULL
            )
        """)

      
