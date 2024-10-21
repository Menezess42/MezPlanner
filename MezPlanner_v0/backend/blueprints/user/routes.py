from flask import Blueprint, request, jsonify
from models import User
from blueprints.app import db, bcrypt

user = Blueprint("user", __name__)


# Create
@user.route("/userCreate", methods=["POST"])
def create_user():
    data = request.get_json()
    # Here I want tu use Bcrypt from flask
    password = bcrypt.generate_password_hash(data.get("password")).decode('utf-8')
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

# Delete

# Alter


# @dayplanner.route("/tasks", methods=["POST"])
# def create_task():
#     data = request.get_json()  # Pega os dados enviados pelo front no formato JSON
#     new_task = Task(
#         name=data.get("name"),
#         description=data.get("description"),
#         start_time=data.get("start_time"),
#         end_time=data.get("end_time"),
#     )
#     db.session.add(new_task)  # Adiciona a nova task no banco
#     db.session.commit()  # Confirma a operação no banco
#     return jsonify({"message": "Task criada com sucesso!"}), 201
