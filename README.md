# CryptoTradingBot - Улучшенная версия от Grok 🚀

## Основные улучшения и новые фичи:
- **Много-биржевая поддержка** через CCXT (Binance, Bybit и др.)
- **Веб-дашборд** с Flask + Plotly графиками
- **Risk Management**: stop-loss, take-profit, position sizing
- **Telegram уведомления** о сделках
- **Backtesting** и оптимизация стратегий
- **Логирование**, retries, error handling
- **Docker** поддержка
- **Безопасность**: .env, wallet validation
- SQLite с миграциями

## Установка
1. `git clone https://github.com/ssssDeMoNssss/CryptoTradingBot.git`
2. `pip install -r requirements.txt`
3. Настрой .env
4. `python main.py`

## Структура
- `core/` - торговля
- `web/` - дашборд
- `db/` - база
- `strategies/` - стратегии

