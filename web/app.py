from flask import Flask, render_template_string, jsonify
import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_API_KEY', ''),
        'secret': os.getenv('BINANCE_API_SECRET', ''),
    })
    
    @app.route('/')
    def dashboard():
        html = '''
        <!DOCTYPE html>
        <html>
        <head><title>Advanced Crypto Bot Dashboard</title>
        <style>body {font-family: Arial; background: #0a0a0a; color: #00ff00; padding: 20px;}</style>
        </head>
        <body>
            <h1>🚀 Crypto Trading Bot - Advanced Dashboard</h1>
            <p>ML Strategies & Backtesting Enabled</p>
            <div id="status">Loading...</div>
            <script>
                function refresh() {
                    fetch('/api/status').then(r=>r.json()).then(data => {
                        document.getElementById('status').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
                    });
                }
                setInterval(refresh, 15000);
                refresh();
            </script>
        </body>
        </html>
        '''
        return render_template_string(html)
    
    @app.route('/api/status')
    def status():
        try:
            balance = exchange.fetch_balance()
            return jsonify({'balance': balance, 'status': 'online'})
        except Exception as e:
            return jsonify({'error': str(e)})
    return app
