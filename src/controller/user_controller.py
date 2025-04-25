from flask import Blueprint
from sqlalchemy import text
from src.config.extensions import db

user_blueprint = Blueprint('main', __name__)

@user_blueprint.route('/')
def hello():
    return "Hello, Flask!"

@user_blueprint.route('/db-check')
def db_check():
    try:
        db.session.execute(text('SELECT 1'))
        return "✅ PostgreSQL connected!"
    except Exception as e:
        return f"❌ Connection failed: {str(e)}"
