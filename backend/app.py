from flask import Flask, jsonify
from routes.marketplace import marketplace
from routes.transactions import transactions

from config import Config
from extensions import db, migrate, bcrypt, jwt

# Models
from models.user import User
from models.wallet import Wallet
from models.energy_asset import EnergyAsset
from models.energy_listing import EnergyListing

# Blueprints
from routes.auth import auth
from routes.energy_assets import assets

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
jwt.init_app(app)

# Register routes
app.register_blueprint(auth)
app.register_blueprint(assets)
app.register_blueprint(marketplace)
app.register_blueprint(transactions)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to GridLink API",
        "version": "1.0",
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(debug=True)