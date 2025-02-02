from flask import Blueprint, request, jsonify
from blueprints.task.models import Task
from backend.blueprints.app import db

task = Blueprint("task", __name__)

# Create
@ task.route("/taskCreate", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(
            name = data.get("name"),
            description=data.get("description"),
            color = data.get("data"),
            template = data.get("color"),
            weekdays = int(data.get("weekdays")),
            usr_id = int(data.get("usr_id")))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message:" "Stock created successfully!"}), 201

# Read
@task.route("/taskGet/<int:stock_id>", methods=["GET"])
def get_task(tsk_id):
    task = task.query.filter_by(tsk_id=tsk_id).one()
    print(task.tsk_id)
    if task:
        task_info = {
                "name": task.name,
                "description": task.description,
                "color": task.color,
                "template": task.template, 
                "weekdays": task.weekdays,
                }
        return jsonify(task_info), 200
    return jsonify({"error": "Task not found, invalid uID or no existent stock"}), 401


# Updtae
@task.route("/taskUpdate/<int:tsk_id>", methods=["PUT"])
def update_task(tsk_id):
    data = request.get_json()
    task = db.session.get(Task, tsk_id)
    if task:
        task.name = data.get("name", task.name),
        task.description = data.get("description", task.description),
        task.color = data.get("color", task.color),
        task.template = data.get("template", task.template),
        task.weekdays = data.get("weekdays", task.weekdays)

        db.session.commit()
        return jsonify({"message": "Task updated successfully"}), 200
    return jsonify({"error": "Task not found"}), 404


# Delete
@task.route("/taskDelete/<int:tsk_id>", methods=["DELTE"])
def delte_task(tsk_id):
    task = db.session.get(Task, tsk_id)
    if not task:
        return jsonify({"error": "task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200
