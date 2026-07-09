from flask_jwt_extended import create_access_token
from extensions import bcrypt
from models.user import User


def login_user(email, password):

    user = User.query.filter_by(email=email).first()

    if user is None:
        return {
            "success": False,
            "message": "Invalid email or password."
        }

    print("Stored hash:", user.password)
    print("Password check:", bcrypt.check_password_hash(user.password, password))

    if not bcrypt.check_password_hash(user.password, password):
        return {
            "success": False,
            "message": "Invalid email or password."
        }

    token = create_access_token(identity=str(user.id))

    return {
        "success": True,
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "gridlink_id": user.gridlink_id
        }
    }