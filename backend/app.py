from flask import Flask, jsonify

from config import Config
from extensions import db, migrate
from models.user import User
from models.wallet import Wallet

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def home():
    return jsonify({
        "message": "GridLink API is running!",
        "database": "Connected",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(debug=True)