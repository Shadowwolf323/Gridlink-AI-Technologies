from flask import Blueprint, request, jsonify

from services.energy_asset_service import (
    create_asset,
    get_all_assets,
    get_asset,
    update_asset,
    delete_asset
)

assets = Blueprint("assets", __name__)


@assets.route("/assets", methods=["POST"])
def add_asset():

    data = request.get_json()

    asset = create_asset(
        data["user_id"],
        data["asset_type"],
        data["capacity_kw"],
        data.get("location")
    )

    return jsonify(asset), 201


@assets.route("/assets", methods=["GET"])
def list_assets():

    return jsonify(get_all_assets())


@assets.route("/assets/<int:id>", methods=["GET"])
def one_asset(id):

    asset = get_asset(id)

    if not asset:
        return jsonify({"message": "Asset not found"}), 404

    return jsonify(asset)


@assets.route("/assets/<int:id>", methods=["PUT"])
def edit_asset(id):

    asset = update_asset(id, request.get_json())

    if not asset:
        return jsonify({"message": "Asset not found"}), 404

    return jsonify(asset)


@assets.route("/assets/<int:id>", methods=["DELETE"])
def remove_asset(id):

    deleted = delete_asset(id)

    if not deleted:
        return jsonify({"message": "Asset not found"}), 404

    return jsonify({
        "message": "Asset deleted successfully"
    })