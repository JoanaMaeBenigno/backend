from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

from src.config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route('/db-check')
def db_check():
    try:
        # Executes a simple query
        db.session.execute(text('SELECT 1'))
        return "✅ PostgreSQL connected!"
    except Exception as e:
        return f"❌ Connection failed: {str(e)}"

if __name__ == '__main__':
    debug = os.getenv("DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug, port=port)