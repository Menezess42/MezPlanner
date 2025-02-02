from flask import Blueprint, request, jsonify
from blueprints.ownMoney.models import OwnMoney
from backend.blueprints.app import db
from datetime import datetime

ownMoney = Blueprint("ownMoeny", __name__)

# Create
@ownMoney.route("/ownMoneyCreate", methods=["POST"])
def create_ownMoney():
    data = request.get_json()
    new_ownMoney = OwnMoney(
            walet_id = int(data.get("walet_id")),
            invested_value = float(data.get("invested_value")),
            invested_date = datetime.strptime(data.get("invested_date"), "%Y-%m-%dT%H:%M:%S"),
            iStarted_value=bool(data.get("iStarted_value"))
            )
    db.session.add(new_ownMoney)
    db.session.commit()
    return jsonify({"message": "ownMoney created successfully"}), 201

# Read
@ownMoney.route("/ownMoneyRead/<int:own_id>", methods=["GET"])
def read_ownMoney(own_id):
    ownMoney = OwnMoney.query.filter_by(own_id=own_id).one()
    print(ownMoney.own_id)
    if ownMoney:
        ownMoney_info = {
                "walet_id": ownMoney.walet_id,
                "invested_value": ownMoney.invested_value,
                "invested_date": ownMoney.invested_date,
                "iStarted_value": ownMoney.iStarted_value
                }
        return jsonify(ownMoney_info), 200
    return jsonify({"message":"ownMoney not found, invalid oID or no existent ownMoney"}), 404


# Update
@ownMoney.route("/ownMoneyUpdate/<int:own_id>", methods=["PUT"])
def update_ownMoney(own_id):
    data = request.get_json()
    ownMoney = db.session.get(OwnMoney, own_id)
    if ownMoney:
        ownMoney.walet_id = int(data.get("walet_id", ownMoney.walet_id))
        ownMoney.invested_value = float(data.get("invested_value", ownMoney.invested_value))
        ownMoney.invested_date = datetime.strptime(data.get("invested_date", ownMoney.invested_date), "%Y-%m-%dT%H:%M:%S")
        ownMoney.iStarted_value = bool(data.get("iStarted_value", ownMoney.iStarted_value))
        return jsonify({"message": "OwnMoney updated successfully"}), 200
    return jsonify({"error": "OwnMoney not founded"}), 404


# Delete
@ownMoney.route("/ownMoneyDelete/<int:own_id>", methods=["DELETE"])
def delete_ownMoney(own_id):
    ownMoney = db.session.get(OwnMoney, own_id)
    if not ownMoney:
        return jsonify({"error": "OwnMoney not founded"}), 400
    db.session.delete(ownMoney)
    db.session.commit()
    return jsonify({"message": "OwnMoney deleted successfully"}), 200



















