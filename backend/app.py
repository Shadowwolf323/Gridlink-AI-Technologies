from flask import Flask, jsonify

from config import Config
from extensions import db, migrate, bcrypt
from models.user import User
from models.wallet import Wallet
from routes.auth import auth

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
app.register_blueprint(auth)


@app.route("/")
def home():
    return jsonify({
        "message": "GridLink API is running!",
        "database": "Connected",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(debug=True)