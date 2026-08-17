import sqlite3
import os

from contextlib import contextmanager

DB_PATH = 'myvideogamelist.db'

@contextmanager
def get_db_connection():
    """Context manager for SQLite database connection."""
    conn = sqlite3.connect(DB_PATH)
    try:
        # Enable foreign key support in SQLite
        conn.execute("PRAGMA foreign_keys = 1")
        # Return rows as dictionaries
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create sagas table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sagas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        ''')

        # Create games table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                release_date TEXT,
                status TEXT,
                store TEXT,
                saga_id INTEGER,
                FOREIGN KEY (saga_id) REFERENCES sagas (id) ON DELETE SET NULL
            )
        ''')

        conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
