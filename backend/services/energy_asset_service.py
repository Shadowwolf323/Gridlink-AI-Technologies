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

    if not asset:
        return None

    return asset.to_dict()


def update_asset(asset_id, data):

    asset = EnergyAsset.query.get(asset_id)

    if not asset:
        return None

    asset.asset_type = data.get("asset_type", asset.asset_type)
    asset.capacity_kw = data.get("capacity_kw", asset.capacity_kw)
    asset.location = data.get("location", asset.location)
    asset.status = data.get("status", asset.status)

    db.session.commit()

    return asset.to_dict()


def delete_asset(asset_id):

    asset = EnergyAsset.query.get(asset_id)

    if not asset:
        return False

    db.session.delete(asset)
    db.session.commit()

    return True