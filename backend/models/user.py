from extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    account_type = db.Column(
        db.String(20),
        nullable=False
    )  # household, business, admin

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    wallets = db.relationship(
        "Wallet",
        backref="owner",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"