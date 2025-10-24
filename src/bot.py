import os
from binance.client import Client
from dotenv import load_dotenv
import sqlite3

# Загрузка переменных окружения
load_dotenv()

# Инициализация Binance API
client = Client(api_key=os.getenv('BINANCE_API_KEY'), api_secret=os.getenv('BINANCE_API_SECRET'))

# Инициализация базы данных SQLite
def init_db():
    conn = sqlite3.connect('trading.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            quantity REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Пример функции для получения цены
def get_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

if __name__ == "__main__":
    init_db()
    print(f"Текущая цена BTC: {get_price('BTCUSDT')}")
    print("Бот запущен!")