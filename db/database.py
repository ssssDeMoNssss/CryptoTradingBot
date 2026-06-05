import sqlite3
from loguru import logger

def init_db():
    conn = sqlite3.connect('trading.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY, symbol TEXT, side TEXT, price REAL, quantity REAL, timestamp TEXT)''')
    conn.commit()
    conn.close()
    logger.info('Database initialized')