from flask import Blueprint, request, jsonify

from services.auth_service import register_user

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    result = register_user(
        full_name=data["full_name"],
        email=data["email"],
        password=data["password"],
        account_type=data["account_type"]
    )

    return jsonify(result)