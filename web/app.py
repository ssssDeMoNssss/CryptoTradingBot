from flask import Flask, render_template_string

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def dashboard():
        return render_template_string('<h1>Crypto Trading Bot Dashboard</h1><p>Live soon!</p>')
    return app
