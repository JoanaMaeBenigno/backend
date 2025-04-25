from flask import Flask
from flask_cors import CORS
import os

from src.config.config import Config
from src.config.extensions import db
from src.controller.user_controller import user_blueprint
from src.controller.articles_controller import article_blueprint

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(user_blueprint)
app.register_blueprint(article_blueprint)

if __name__ == '__main__':
    debug = os.getenv("DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug, port=port)