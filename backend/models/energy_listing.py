from datetime import datetime
from extensions import db


class EnergyListing(db.Model):
    __tablename__ = "energy_listings"

    id = db.Column(db.Integer, primary_key=True)

    seller_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    energy_amount = db.Column(
        db.Float,
        nullable=False
    )

    price_per_kwh = db.Column(
        db.Float,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        default="available"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "energy_amount": self.energy_amount,
            "price_per_kwh": self.price_per_kwh,
            "status": self.status,
            "created_at": self.created_at.isoformat()
            if self.created_at else None
        }