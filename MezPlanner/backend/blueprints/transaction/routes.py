from flask import Blueprint, request, jsonify
from blueprints.transaction.models import Transaction 
from backend.blueprints.app import db
from datetime import datetime

transaction = Blueprint("transaction", __name__)

# Create
@transaction.route("/transactionCreate", methods=["POST"])
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(
            walet_id = int(data.get("walet_id")),
            stok_id = int(data.get("stok_id")),
            qtde = int(data.get("qtde")),
            price = float(data.get("price")),
            trans_date = datetime.strptime(data.get("trans_date"), "%Y-%m-%dT%H:%M:%S"),
            trans_type=bool(data.get("trans_type"))
            )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({"message:" "User created successfully!"}), 201

# Read
@transaction.route("/transactionRead/<int:trans_id>", methods=["GET"])
def read_transaction(trans_id):
    transaction = Transaction.query.filter_by(trans_id=trans_id).one()
    print(transaction.trans_id)
    if transaction:
        transaction_info = {
                "stock_id": transaction.stock_id,
                "qtde": transaction.qtde,
                "price": transaction.price,
                "trans_date": transaction.trans_date,
                "total_value": transaction.total_value,
                "trans_type": transaction.trans_type
                }
        return jsonify(transaction_info), 200
    return jsonify({"error": "Wallet not found, invalid tID or no existent transaction"}), 401

# Update
@transaction.route("/transactionUpdate/<int:trans_id>", methods=["PUT"])
def update_transaction(trans_id):
    data = request.get_json()
    transaction = db.session.get(transaction, trans_id)
    if transaction:
        transaction.qtde = data.get("qtde", transaction.qtde)
        transaction.price = data.get("price", transaction.price)
        transaction.total_value = data.get("total_value", transaction.total_value)
        transaction.trans_type = data.get("trans_type", transaction.trans_type)
        db.session.commit()
        return jsonify({"message": "Transaction updated successfully"}), 200
    return jsonify({"error": "Transaction not found"}), 404

# Delte
@transaction.route("/transactionDelete/<int:trans_id>", methods=["DELETE"])
def delte_transactioN(trans_id):
    transaction = db.session.get(Transaction, trans_id)
    if not transaction:
        return jsonify({"error": "transaction not found"}), 400
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"message": "transaction deleted successfully"}), 200
















