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

# Update

# Delte
