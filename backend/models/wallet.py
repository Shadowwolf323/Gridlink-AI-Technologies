from extensions import db


class Wallet(db.Model):
    __tablename__ = "wallets"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    wallet_type = db.Column(
        db.String(30),
        nullable=False
    )

    # energy or maintenance
    balance = db.Column(
        db.Float,
        default=0.0
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "wallet_type": self.wallet_type,
            "balance": self.balance,
            "created_at": self.created_at.isoformat()
            if self.created_at else None
        }

    def __repr__(self):
        return f"<Wallet {self.wallet_type}>"