from flask import Blueprint, request, jsonify

from services.transaction_service import (
    buy_energy,
    get_transactions,
    get_transaction,
    delete_transaction
)

transactions = Blueprint("transactions", __name__)


@transactions.route("/transactions/buy", methods=["POST"])
def buy():
    data = request.get_json()

    transaction, error = buy_energy(data)

    if error:
        return jsonify({"message": error}), 400

    return jsonify(transaction), 201


@transactions.route("/transactions", methods=["GET"])
def get_all():
    return jsonify(get_transactions())


@transactions.route("/transactions/<int:id>", methods=["GET"])
def get_one(id):

    transaction = get_transaction(id)

    if not transaction:
        return jsonify({"message": "Transaction not found"}), 404

    return jsonify(transaction)


@transactions.route("/transactions/<int:id>", methods=["DELETE"])
def delete(id):

    success = delete_transaction(id)

    if not success:
        return jsonify({"message": "Transaction not found"}), 404

    return jsonify({
        "message": "Transaction deleted successfully"
    })