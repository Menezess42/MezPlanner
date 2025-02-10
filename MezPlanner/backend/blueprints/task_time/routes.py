from flask import Blueprint, request, jsonify
from backend.blueprints.task_time.models import Task_time
from backend.blueprints.app import db
from datetime import time, datetime

task_time = Blueprint("task_time", __name__)

# Create
@task_time.route("/tasktimeCreate", methods=["POST"])
def create_taskTime():
    data = request.get_json()
    new_taskTime = Task_time(
            startime=time.fromisoformat(data.get("startime")),
            endtime=time.fromisoformat(data.get("endtime")),
            tsk_id = int(data.get("tsk_id")),
            )
    db.session.add(new_taskTime)
    db.session.commit()
    return jsonify({"message": "Task_time created successfully"}), 201


# Read
@task_time.route("/TaskTimeGet/<int:tsktime_id>", methods=["GET"])
def get_taskTime(tsktime_id):
    tasktime = Task_time.query.filter_by(tsktime_id=tsktime_id).one()
    if tasktime:
        tasktime_info={
                "startime": tasktime.startime.strftime("%H:%M:%S"),
                "endtime": tasktime.endtime.strftime("%H:%M:%S"),
                "tsk_id": tasktime.tsk_id,
                }
        return jsonify(tasktime_info), 200
    return jsonify({"error": "task_time not founded"}), 404


# Update
@task_time.route("/TaskTimeUpdate/<int:tsktime_id>", methods=["PUT"])
def update_tasktime(tsktime_id):
    data = request.get_json()
    tasktime = db.session.get(Task_time, tsktime_id)
    if not tasktime:
        return jsonify({"error": "Task_time not found"}), 404
    try:
        tasktime.startime = datetime.strptime(data["startime"], "%H:%M:%S").time()
        tasktime.endtime = datetime.strptime(data["endtime"], "%H:%M:%S").time()
    except ValueError:
        return jsonify({"error": "Invalid time format. Use HH:MM:SS"}), 400

    db.session.commit()
    return jsonify({"message": "Task_time updated successfully"}), 200


# Delete
@task_time.route("/tasktimeDelete/<int:tsktime_id>", methods=["DELETE"])
def delete_tasktime(tsktime_id):
    tasktime = db.session.get(Task_time, tsktime_id)
    if not tasktime:
        return jsonify({"Error": {"Tasktime not found"}}), 404
    db.session.delete(tasktime)
    db.session.commit()
    return jsonify({"Message": "Task_time deleted successfully"}), 200



