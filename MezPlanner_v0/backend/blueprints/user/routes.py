from flask import Blueprint, request, jsonify
from models import User
from blueprints.app import db

user = Blueprint("user", __name__)


# Create
@user.route("/userCreate", methods=["POST"])
def create_user():
    data = request.get_json()
    # password = bcrypt IM continuing from here, my internet drop today.
    new_user = User(
        username=data.get("username"),
        password=password,
    )


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
