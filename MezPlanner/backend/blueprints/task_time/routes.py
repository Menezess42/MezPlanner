from flask import Blueprint, request, jsonify
from blueprints.task_time.models import Task_time
from backend.blueprints.app import db
from datetime import time

task_time = Blueprint("task_time", __name__)

# Create
@task_time.route("/tasktimeCreate", methods=["POST"])
def create_taskTime():
    data = request.get_json()
    new_taskTime = Task_time(
            startime = time(data.get("starttime")),
            endtime = time(data.get("endtime")),
            tsk_id = int(data.get("tsk_id"))
            )
    db.session.add(new_taskTime)
    db.session.commit()
    return jsonify({"message": "Task_time created successfully"}), 201


# Read
@task_time.route("/TasktimeRead/<int:tsktime_id>", methods=["GET"])
def get_taskTime(tsktime_id):
    tasktime = Task_time.query.filter_by(tsktime_id=tsktime_id).one()
    print(tasktime.tsktime_id)
    if tasktime:
        tasktime_info={
                "startime": tasktime.startime,
                "endtime": tasktime.endtime,
                }
        return jsonify(tasktime_info), 200
    return jsonify({"error": "task_time not founded"}), 404


# Update
@task_time.route("tasktimeUpdate/<int:tsktime_id>", methods=["POST"])
def update_tasktime(tsktime_id):
    data = request.get_json()
    tasktime = db.session.get(Task_time, tsktime_id)
    if tasktime:
        tasktime.startime=data.get("startime", tasktime.startime)
        tasktime.endtime = data.get("endtime", tasktime.endtime)
        db.session.commit()
        return jsonify({"message": "Task_time updated successfully"}), 200
    return jsonify({"error": "Task_time not found"}), 404


# Delete
@task_time.route("/tasktimeDelete/<int:tsktime_id>", methods=["DELETE"])
def delete_tasktime(tsk_id):
    tasktime = db.session.get(Task_time, tsk_id)
    if not tasktime:
        return jsonify({"Error": {"Tasktime not found"}}), 404
    db.session.delete(tasktime)
    db.session.commit()
    return jsonify({"Message": "Tasktime deleted successfully"}), 200



