from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env into environment variables

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    debug = os.getenv("DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug, port=port)