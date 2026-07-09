from extensions import db
from models.energy_listing import EnergyListing


def create_listing(seller_id, energy_amount, price_per_kwh):

    listing = EnergyListing(
        seller_id=seller_id,
        energy_amount=energy_amount,
        price_per_kwh=price_per_kwh,
        status="available"
    )

    db.session.add(listing)
    db.session.commit()

    return listing.to_dict()


def get_all_listings():

    listings = EnergyListing.query.all()

    return [listing.to_dict() for listing in listings]


def get_listing(listing_id):

    listing = EnergyListing.query.get(listing_id)

    if not listing:
        return None

    return listing.to_dict()


def update_listing(listing_id, data):

    listing = EnergyListing.query.get(listing_id)

    if not listing:
        return None

    listing.energy_amount = data.get(
        "energy_amount",
        listing.energy_amount
    )

    listing.price_per_kwh = data.get(
        "price_per_kwh",
        listing.price_per_kwh
    )

    listing.status = data.get(
        "status",
        listing.status
    )

    db.session.commit()

    return listing.to_dict()


def delete_listing(listing_id):

    listing = EnergyListing.query.get(listing_id)

    if not listing:
        return False

    db.session.delete(listing)
    db.session.commit()

    return True