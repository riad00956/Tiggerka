import sqlite3
import config

def get_connection():
    conn = sqlite3.connect(config.DATABASE_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
