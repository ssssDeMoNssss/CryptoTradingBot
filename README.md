# CryptoTradingBot v6.0 - Advanced ML + RL Trading Bot

**Optimized for Ubuntu 24.04.4**

Professional crypto trading bot with multi-exchange support, ML/LSTM/RL strategies, advanced backtesting, web dashboard.

## Features
- Multi-agent RL, Ensemble models, LSTM, Sentiment analysis
- CCXT support for Binance, Bybit, OKX, KuCoin, DeFi
- Dash web UI with real-time charts
- Hyperparameter optimization with Optuna
- Docker support
- Ubuntu 24.04 ready (systemd service ready)

## Installation on Ubuntu 24.04
```bash
sudo apt update && sudo apt install python3-pip python3-venv git -y
git clone https://github.com/ssssDeMoNssss/CryptoTradingBot.git
cd CryptoTradingBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env
python main.py --strategy ensemble
```

See full docs in docs/ folder.