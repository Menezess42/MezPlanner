from flask import Blueprint, request, jsonify
from backend.blueprints.user.models import User
from backend.blueprints.app import db, bcrypt
from datetime import datetime

user = Blueprint("user", __name__)

# Create
@user.route("/userCreate", methods=["POST"])
def create_user():
    data = request.get_json()
    # Here I want tu use Bcrypt from flask
    password = bcrypt.generate_password_hash(data.get("password")).decode("utf-8")
    new_user = User(
        name=data.get("name"),
        email=data.get("email"),
        password=password,
        birthday=datetime.strptime(data.get("birthday"), "%Y-%m-%d").date(),
        createdat=datetime.now(),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

# get
@user.route("/userGet/<int:usr_id>", methods=["GET"])
def get_user(usr_id):
    user = User.query.filter_by(usr_id=usr_id).one()
    print(user.usr_id)
    if user:
        user_info = {
            "name": user.name,
            "email": user.email,
            "birthday": user.birthday,
            "createdat": user.createdat,
        }
        return jsonify(user_info), 200
    return jsonify({"error": "User not found, invalid uID or no existent user"}), 401


# login
@user.route("/userLogin", methods=["GET", "POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    print(password)
    print(bcrypt.check_password_hash(user.password, password))
    if user and bcrypt.check_password_hash(user.password, password):
        user_info = {
            "name": user.name,
            "email": user.email,
            "birthday": user.birthday,
            "createdat": user.createdat,
        }
        return jsonify(user_info), 200
    return jsonify({"error": "Invalid email or password"}), 401


# Delete
@user.route("/userDelete/<int:usr_id>", methods=["DELETE"])
def delete_user(usr_id):
    user = db.session.get(User, usr_id)
    if not user:
        return jsonify({"error": "user not found"}), 400

    related_objects = {
        "tasks": ("tsk_id", user.tasks),
        "intervals": ("intvl_id", user.intervals),
        "wallets": ("wallet_id", user.wallets),
    }

    conflicts = {
        relation: [getattr(obj, pk) for obj in objects]
        for relation, (pk, objects) in related_objects.items()
        if objects
    }

    if conflicts:
        return (
            jsonify(
                {
                    "error": "Cannot delete user, related objects exist.",
                    "details": conflicts,
                }
            ),
            400,
        )

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200


# Alter
@user.route("/userUpdate/<int:usr_id>", methods=["PUT"])
def update_user(usr_id):
    data = request.get_json()
    user = db.session.get(User, usr_id)

    if user:
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        user.birthday = data.get("birthday", user.birthday)
        if "password" in data:
            user.password = bcrypt.generate_password_hash(data["password"]).decode(
                "utf-8"
            )

        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    return jsonify({"error": "User not found"}), 404
