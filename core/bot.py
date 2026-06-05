import ccxt
import os
from dotenv import load_dotenv
from loguru import logger
from db.database import init_db
from web.app import create_app
import threading
from strategies.simple_ma import simple_ma_strategy
from strategies.ml_strategy import ml_strategy
from backtesting.advanced_backtest import run_backtest

load_dotenv()

class TradingBot:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': os.getenv('BINANCE_API_KEY'),
            'secret': os.getenv('BINANCE_API_SECRET'),
        })
        init_db()
        self.app = create_app()
        logger.info('Trading Bot initialized with ML & Backtesting')

    def run(self):
        # Run backtest on start
        try:
            run_backtest(self.exchange)
        except Exception as e:
            logger.error(f'Backtest error: {e}')
        
        # Start web server
        threading.Thread(target=self.app.run, kwargs={'debug': False, 'port': 5000}).start()
        logger.info('Web dashboard running at http://localhost:5000')
        
        # Main loop with strategies
        while True:
            try:
                signal = ml_strategy(self.exchange)  # or simple_ma
                logger.info(f'ML Signal: {signal}')
                # Implement trading logic here
            except Exception as e:
                logger.error(e)
            import time
            time.sleep(60)

if __name__ == '__main__':
    bot = TradingBot()
    bot.run()
