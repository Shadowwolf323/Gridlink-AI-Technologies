from extensions import db
from models.energy_asset import EnergyAsset


def create_asset(user_id, asset_type, capacity_kw, location):

    asset = EnergyAsset(
        user_id=user_id,
        asset_type=asset_type,
        capacity_kw=capacity_kw,
        location=location
    )

    db.session.add(asset)
    db.session.commit()

    return asset.to_dict()


def get_all_assets():

    assets = EnergyAsset.query.all()

    return [asset.to_dict() for asset in assets]


def get_asset(asset_id):

    asset = EnergyAsset.query.get(asset_id)

    if asset is None:
        return None

    return asset.to_dict()