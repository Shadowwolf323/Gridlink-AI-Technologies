from models.user import User
from models.wallet import Wallet


def get_profile(user_id):

    user = User.query.get(user_id)

    if not user:
        return {
            "success": False,
            "message": "User not found."
        }

    wallets = Wallet.query.filter_by(user_id=user.id).all()

    wallet_data = []

    for wallet in wallets:
        wallet_data.append({
            "wallet_type": wallet.wallet_type,
            "balance": wallet.balance
        })

    return {
        "success": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "gridlink_id": user.gridlink_id,
            "email": user.email,
            "created_at": user.created_at.isoformat() if user.created_at else None
        },
        "wallets": wallet_data
    }