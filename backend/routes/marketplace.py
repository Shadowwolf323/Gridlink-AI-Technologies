from flask import Blueprint, request, jsonify

from services.marketplace_service import (
    create_listing,
    get_all_listings,
    get_listing,
    update_listing,
    delete_listing
)

marketplace = Blueprint("marketplace", __name__)


@marketplace.route("/marketplace/listings", methods=["POST"])
def create():

    data = request.get_json()

    listing = create_listing(
        seller_id=data["seller_id"],
        energy_amount=data["energy_amount"],
        price_per_kwh=data["price_per_kwh"]
    )

    return jsonify(listing), 201


@marketplace.route("/marketplace/listings", methods=["GET"])
def get_all():

    return jsonify(get_all_listings())


@marketplace.route("/marketplace/listings/<int:id>", methods=["GET"])
def get_one(id):

    listing = get_listing(id)

    if not listing:
        return jsonify({"message": "Listing not found"}), 404

    return jsonify(listing)


@marketplace.route("/marketplace/listings/<int:id>", methods=["PUT"])
def update(id):

    listing = update_listing(
        id,
        request.get_json()
    )

    if not listing:
        return jsonify({"message": "Listing not found"}), 404

    return jsonify(listing)


@marketplace.route("/marketplace/listings/<int:id>", methods=["DELETE"])
def delete(id):

    success = delete_listing(id)

    if not success:
        return jsonify({"message": "Listing not found"}), 404

    return jsonify({
        "message": "Listing deleted successfully"
    })