from flask import Blueprint, request, jsonify
from backend.blueprints.wallet.models import Wallet
from backend.blueprints.app import db
from datetime import datetime


wallet = Blueprint("wallet", __name__)

# Create
@wallet.route("/walletCreate", methods=["POST"])
def create_wallet():
    data = request.get_json()
    new_wallet = Wallet(
            name = data.get("name"),
            current_value = float(data.get("current_value")),
            highest_value=float(data.get("highest_value")),
            highest_value_day = datetime.strptime(data.get("highest_value_day"), "%Y-%m-%dT%H:%M:%S"),
            stock_value = float(data.get("stock_value")),
            own_money_value = float(data.get("own_money_value")),
            credit = float(data.get("credit")),
            only_stock_value=float(data.get("only_stock_value")),
            usr_id = int(data.get("usr_id"))
            )
    db.session.add(new_wallet)
    db.session.commit()
    return jsonify({"message": "Wallet created successfully!"}), 201

# Read
@wallet.route("/walletGet/<int:walet_id>", methods=["GET"])
def read_wallet(walet_id):
    wallet = Wallet.query.filter_by(walet_id=walet_id).one()
    print(wallet.walet_id)
    if wallet:
        wallet_info = {
                "name": wallet.name,
                "current_value": wallet.current_value,
                "highest_value": wallet.highest_value,
                "highest_value_day": wallet.highest_value_day,
                "stock_value": wallet.stock_value,
                "own_money_value": wallet.own_money_value,
                "credt": wallet.credit,
                "only_stock_value": wallet.only_stock_value,
                "usr_id": wallet.usr_id,
                }
        return jsonify(wallet_info), 200
    return jsonify({"error": "Wallet not found, invalid wID or no existent wallet"}), 401

# Update
@wallet.route("/walletUpdate/<int:walet_id>", methods=["PUT"])
def update_wallet(walet_id):
    data = request.get_json()
    wallet = db.session.get(Wallet, walet_id)
    if wallet:
        wallet.name = data.get("name", wallet.name)
        wallet.current_value=float(data.get("current_value", wallet.current_value))
        wallet.highest_value=float(data.get("highest_value", wallet.highest_value))
        wallet.highest_value_day = datetime.strptime(data.get("highest_value_day", wallet.highest_value_day), "%Y-%m-%dT%H:%M:%S")
        wallet.stock_value=float(data.get("stock_value", wallet.stock_value))
        wallet.own_money_value = float(data.get("own_money_value", wallet.own_money_value))
        wallet.credit = float(data.get("credit", wallet.credit))
        wallet.only_stock_value = float(data.get("only_stock_value", wallet.only_stock_value))
        wallet.usr_id = int(data.get("usr_id", wallet.usr_id))
        db.session.commit()
        return jsonify({"message": "Wallet updated successfully"}), 200
    return jsonify({"error": "Wallet not found"}), 404

# Delete
@wallet.route("/walletDelete/<int:walet_id>", methods=["DELETE"])
def delete_wallet(walet_id):
    wallet = db.session.get(Wallet, walet_id)
    if not wallet:
        return jsonify({"Error": "Wallet not found"}), 400
    db.session.delete(wallet)
    db.session.commit()
    return jsonify({"message": "Wallet deleted successfully"}), 200














