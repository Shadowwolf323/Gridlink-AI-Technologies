from extensions import db, bcrypt
from models.user import User
from models.wallet import Wallet


def register_user(full_name, email, password, account_type):

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered."
        }

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(
        full_name=full_name,
        email=email,
        password=hashed_password,
        account_type=account_type
    )

    db.session.add(user)
    db.session.commit()

    energy_wallet = Wallet(
        user_id=user.id,
        wallet_type="energy",
        balance=0
    )

    maintenance_wallet = Wallet(
        user_id=user.id,
        wallet_type="maintenance",
        balance=0
    )

    db.session.add(energy_wallet)
    db.session.add(maintenance_wallet)

    db.session.commit()

    return {
        "success": True,
        "message": "Registration successful."
    }