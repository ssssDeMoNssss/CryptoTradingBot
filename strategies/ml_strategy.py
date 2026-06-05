import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import ccxt

def prepare_features(df):
    df = df.copy()
    df['return'] = df['close'].pct_change()
    df['ma_short'] = df['close'].rolling(10).mean()
    df['ma_long'] = df['close'].rolling(50).mean()
    df['volatility'] = df['close'].rolling(20).std()
    df = df.dropna()
    features = df[['ma_short', 'ma_long', 'volatility', 'volume']].values
    target = np.where(df['return'].shift(-1) > 0, 1, 0)
    return features, target

def ml_strategy(exchange, symbol='BTC/USDT', timeframe='1h'):
    bars = exchange.fetch_ohlcv(symbol, timeframe, limit=500)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    X, y = prepare_features(df)
    if len(X) < 50:
        return 'hold'
    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    latest = X[-1:].reshape(1, -1)
    prediction = model.predict(latest)[0]
    return 'buy' if prediction == 1 else 'sell'