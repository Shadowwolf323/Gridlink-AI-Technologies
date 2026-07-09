from extensions import db
from models.transaction import Transaction
from models.energy_listing import EnergyListing
from models.wallet import Wallet


def buy_energy(data):
    buyer_id = data["buyer_id"]
    listing_id = data["listing_id"]
    energy_requested = data["energy_amount"]

    listing = EnergyListing.query.get(listing_id)

    if not listing:
        return None, "Listing not found"

    if listing.status != "available":
        return None, "Listing is not available"

    if listing.seller_id == buyer_id:
        return None, "You cannot buy your own energy"

    if energy_requested > listing.energy_amount:
        return None, "Not enough energy available"

    buyer_wallet = Wallet.query.filter_by(user_id=buyer_id).first()
    seller_wallet = Wallet.query.filter_by(user_id=listing.seller_id).first()

    if not buyer_wallet:
        return None, "Buyer wallet not found"

    if not seller_wallet:
        return None, "Seller wallet not found"

    total_price = energy_requested * listing.price_per_kwh

    if buyer_wallet.balance < total_price:
        return None, "Insufficient wallet balance"

    buyer_wallet.balance -= total_price
    seller_wallet.balance += total_price

    listing.energy_amount -= energy_requested

    if listing.energy_amount == 0:
        listing.status = "sold"

    transaction = Transaction(
        buyer_id=buyer_id,
        seller_id=listing.seller_id,
        listing_id=listing.id,
        energy_amount=energy_requested,
        price_per_kwh=listing.price_per_kwh,
        total_price=total_price,
        status="completed"
    )

    db.session.add(transaction)
    db.session.commit()

    return transaction.to_dict(), None


def get_transactions():
    return [t.to_dict() for t in Transaction.query.all()]


def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if transaction:
        return transaction.to_dict()

    return None


def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return False

    db.session.delete(transaction)
    db.session.commit()

    return True