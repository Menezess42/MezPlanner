from flask import Blueprint, request, jsonify
from blueprints.interval.models import Interval
from backend.blueprints.app import db
from datetime import datetime

intervals = Blueprint("interval", __name__)


# Create
@intervals.route("/intervalCreate", methods=["POST"])
def create_interval():
    data = request.get_json()
    new_interval = Interval(
            intvl_type = data.get("intvl_type"),
            weekdays = int(data.get("weekdays")),
            valid_startdate = datetime.strptime(data.get("valid_startdate"), "%Y-%m-%d").date(),
            valid_endate=datetime.strptime(data.get("valid_endate"), "%Y-%m-%d").get(),
            usr_id = int(data.get("usr_id"))
            )
    db.session.add(new_interval)
    db.session.commit()
    return jsonify({"message": "Interval created successfully!"}), 201

# Read
@intervals.route("/intervalGet/<int:intvl_id>", methods=["GET"])
def get_interval(intvl_id):
    interval = Interval.query.filter_by(intvl_id=intvl_id).one()
    print(interval.intvl_id)
    if interval:
        interval_info = {
                "intvl_type": interval.intvl_type,
                "weekdays": interval.weekdays,
                "valid_startdate": interval.valid_startdate,
                "valid_endate": interval.valid_endate
                }
        return jsonify(interval_info), 200
    return jsonify({"error": "Interval not found, invalid iID or no existent user"}), 401

# update
@intervals.route("/intervalUpdate/<int:intvl_id>", methods=["POST"])
def update_interval(intvl_id):
    data = request.get_json()
    interval = db.session.get(Interval, intvl_id)
    if interval:
        interval.intvl_type = data.get("intvl_type", interval.intvl_type),
        interval.weekdays = data.get("weekdays", interval.weekdays),
        interval.valid_startdate = data.get("valid_startdate", interval.valid_startdate),
        interval.valid_endate = data.get("valid_endate", interval.valid_endate)
        db.session.commit()
        return jsonify({"message": "Interval updated successfully"}), 200
    return jsonify({"error": "Interval not found"}), 404

# Delete
@intervals.route("/intervalDelete/<int:intvl_id>", methods=["DELETE"])
def delete_interval(intvl_id):
    interval = db.session.get(Interval, intvl_id),
    if not interval:
        return jsonify({"error": "Interval not found"}), 400
    db.session.delete(interval)
    db.session.commit()
    return jsonify({"message": "Interval deleted successfully"}), 200
