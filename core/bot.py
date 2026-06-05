import ccxt
import os
from dotenv import load_dotenv
from loguru import logger
from db.database import init_db
from web.app import create_app
import threading

load_dotenv()

class TradingBot:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': os.getenv('BINANCE_API_KEY'),
            'secret': os.getenv('BINANCE_API_SECRET'),
        })
        init_db()
        self.app = create_app()
        logger.info('Trading Bot initialized')

    def run(self):
        # Start web server in thread
        threading.Thread(target=self.app.run, kwargs={'debug': False, 'port': 5000}).start()
        logger.info('Web dashboard running at http://localhost:5000')
        # Main trading loop here
        while True:
            pass  # Implement strategy

if __name__ == '__main__':
    bot = TradingBot()
    bot.run()
