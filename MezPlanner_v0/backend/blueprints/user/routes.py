from flask import Blueprint, request, jsonify
from blueprints.user.models import User
from blueprints.app import db, bcrypt

user = Blueprint("user", __name__)


# Create
@user.route("/userCreate", methods=["POST"])
def create_user():
    data = request.get_json()
    # Here I want tu use Bcrypt from flask
    password = bcrypt.generate_password_hash(data.get("password")).decode("utf-8")
    new_user = User(
        username=data.get("username"),
        password=password,
        email=data.get("email"),
        birthday=data.get("birthday"),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201


# Get
@user.route("/userGet", methods=["GET"])
def get_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        user_info = {
            "username": user.username,
            "email": user.email,
            "birthday": user.birthday,
            "created_at": user.createdat
        }
        return jsonify(user_info), 200
    return jsonify({"error": "Invalid email or password"}), 401

# Delete
@user.route("/userDelete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}),200
    return jsonify({"error": "User not found"}), 404

# Alter
@user.route("/userUpdate/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)

    if user:
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.birthday = data.get("birthday", user.birthday)

        if "password" in data:
            user.password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    return jsonify({"error": "User not found"}), 404
        
