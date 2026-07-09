from datetime import datetime
from extensions import db


class EnergyAsset(db.Model):
    __tablename__ = "energy_assets"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    asset_type = db.Column(
        db.String(50),
        nullable=False
    )

    capacity_kw = db.Column(
        db.Float,
        nullable=False
    )

    location = db.Column(
        db.String(255),
        nullable=True
    )

    status = db.Column(
        db.String(50),
        default="active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "asset_type": self.asset_type,
            "capacity_kw": self.capacity_kw,
            "location": self.location,
            "status": self.status,
            "created_at": (
                self.created_at.isoformat()
                if self.created_at else None
            )
        }