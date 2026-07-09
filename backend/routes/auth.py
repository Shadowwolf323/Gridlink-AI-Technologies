from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.auth_service import register_user
from services.login_service import login_user
from services.profile_service import get_profile

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    result = register_user(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )

    return jsonify(result)


@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    result = login_user(
        email=data["email"],
        password=data["password"]
    )

    return jsonify(result)


@auth.route("/me", methods=["GET"])
@jwt_required()
def me():

    user_id = get_jwt_identity()

    result = get_profile(user_id)

    return jsonify(result)




