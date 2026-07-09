from extensions import db
from models.transaction import Transaction
from models.energy_listing import EnergyListing
from models.wallet import Wallet


def buy_energy(data):
    buyer_id = data.get("buyer_id")
    listing_id = data.get("listing_id")

    if not buyer_id or not listing_id:
        return None, "buyer_id and listing_id are required"

    listing = EnergyListing.query.get(listing_id)

    if not listing:
        return None, "Listing not found"

    if listing.status != "available":
        return None, "Listing is no longer available"

    total_price = listing.energy_amount * listing.price_per_kwh

    buyer_wallet = Wallet.query.filter_by(
        user_id=buyer_id,
        wallet_type="energy"
    ).first()

    if not buyer_wallet:
        return None, "Buyer wallet not found"

    if buyer_wallet.balance < total_price:
        return None, "Insufficient balance"

    seller_wallet = Wallet.query.filter_by(
        user_id=listing.seller_id,
        wallet_type="energy"
    ).first()

    if not seller_wallet:
        return None, "Seller wallet not found"

    buyer_wallet.balance -= total_price
    seller_wallet.balance += total_price

    listing.status = "sold"

    transaction = Transaction(
        buyer_id=buyer_id,
        seller_id=listing.seller_id,
        listing_id=listing.id,
        energy_amount=listing.energy_amount,
        total_price=total_price
    )

    db.session.add(transaction)
    db.session.commit()

    return transaction.to_dict(), None


def get_transactions():
    return [
        transaction.to_dict()
        for transaction in Transaction.query.all()
    ]


def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return None

    return transaction.to_dict()


def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return False

    db.session.delete(transaction)
    db.session.commit()

    return True