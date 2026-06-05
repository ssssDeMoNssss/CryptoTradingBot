import pandas as pd
import ccxt

def simple_ma_strategy(exchange, symbol='BTC/USDT', timeframe='1h'):
    bars = exchange.fetch_ohlcv(symbol, timeframe, limit=100)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['ma_short'] = df['close'].rolling(10).mean()
    df['ma_long'] = df['close'].rolling(50).mean()
    # Logic for buy/sell
    return 'buy' if df['ma_short'].iloc[-1] > df['ma_long'].iloc[-1] else 'sell'