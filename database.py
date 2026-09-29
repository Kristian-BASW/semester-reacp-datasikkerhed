import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("app.db")


def connect() -> sqlite3.Connection:
    return sqlite3.connect(database_path)


def initialize_database() -> None:
    with connect() as database:
        database.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)

      
