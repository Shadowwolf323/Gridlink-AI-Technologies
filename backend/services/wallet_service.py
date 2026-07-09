from extensions import db
from models.wallet import Wallet


def create_wallet(data):
    wallet = Wallet(
        user_id=data["user_id"],
        wallet_type=data["wallet_type"],
        balance=data.get("balance", 0.0)
    )

    db.session.add(wallet)
    db.session.commit()

    return wallet


def get_wallets():
    return Wallet.query.all()


def get_wallet(wallet_id):
    return Wallet.query.get(wallet_id)


def update_wallet(wallet_id, data):
    wallet = Wallet.query.get(wallet_id)

    if not wallet:
        return None

    wallet.wallet_type = data.get("wallet_type", wallet.wallet_type)
    wallet.balance = data.get("balance", wallet.balance)

    db.session.commit()

    return wallet


def delete_wallet(wallet_id):
    wallet = Wallet.query.get(wallet_id)

    if not wallet:
        return False

    db.session.delete(wallet)
    db.session.commit()

    return True


def get_wallet_by_user(user_id, wallet_type="energy"):
    return Wallet.query.filter_by(
        user_id=user_id,
        wallet_type=wallet_type
    ).first()