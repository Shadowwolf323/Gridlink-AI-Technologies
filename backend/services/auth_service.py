from extensions import db, bcrypt
from models.user import User
from models.wallet import Wallet


def register_user(username, email, password):

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered."
        }

    # Hash password
    hashed_password = bcrypt.generate_password_hash(
        password,
        rounds=12
    ).decode("utf-8")

    # DEBUG
    print("=" * 60)
    print("REGISTER DEBUG")
    print("Username :", username)
    print("Email    :", email)
    print("Password :", password)
    print("Hash     :", hashed_password)
    print("=" * 60)

    # Create user
    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    # Generate GridLink ID
    user.gridlink_id = f"GL-2026-{user.id:06d}"
    db.session.commit()

    # Create Energy Wallet
    energy_wallet = Wallet(
        user_id=user.id,
        wallet_type="energy",
        balance=0.0
    )

    # Create Maintenance Wallet
    maintenance_wallet = Wallet(
        user_id=user.id,
        wallet_type="maintenance",
        balance=0.0
    )

    db.session.add(energy_wallet)
    db.session.add(maintenance_wallet)
    db.session.commit()

    return {
        "success": True,
        "message": "Registration successful.",
        "gridlink_id": user.gridlink_id
    }