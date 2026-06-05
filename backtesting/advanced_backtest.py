import pandas as pd
import ccxt
from strategies.simple_ma import simple_ma_strategy

def run_backtest(exchange, symbol='BTC/USDT', timeframe='1h', initial_capital=10000):
    bars = exchange.fetch_ohlcv(symbol, timeframe, limit=1000)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['signal'] = 0
    for i in range(50, len(df)):
        signal = simple_ma_strategy(exchange, symbol, timeframe)
        df.loc[i, 'signal'] = 1 if signal == 'buy' else -1
    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']
    df['cumulative'] = (1 + df['strategy_returns']).cumprod() * initial_capital
    final_value = df['cumulative'].iloc[-1]
    print(f'Advanced Backtest Result for {symbol}: ${final_value:.2f}')
    return final_value