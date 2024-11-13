from flask import Blueprint, request, jsonify
from blueprints.task.models import Task
from backend.blueprints.app import db
from datetime import datetime

task = Blueprint("task", __name__)

#Create
@task.route("/taskCreate", method=["POST"])
def create_task():
    data = request.get_json()
    try:
        startime = datetime.strptime(data.get("startime"), "%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return {"error": "Formato de startime inválido. Use '%Y-%m-%d %H:%M:%S'."}, 400
    try:
        endtime = datetime.strptime(data.get("endtime"), "%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return {"error": "Formato de endtime inválido. Use '%Y-%m-%d %H:%M:%S'."}, 400
    new_task = Task(
        taskname = data.get("taskname"),
        description = data.get("description"),
        startime = startime,
        endtime = endtime,
        template = data.get("template"),
        weekdays = data.get("weekdays")
    )
    db.session.add(new_task)
    db.session.commit()
    return {"message": "Task criada com sucesso"}, 201
