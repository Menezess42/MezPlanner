from flask import Blueprint, request, jsonify
from blueprints.stocks.models import Stock
from backend.blueprints.app import db
from datetime import datetime

stock = Blueprint("stock", __name__)


# Create
@stock.route("/stockCreate", methods=["POST"])
def create_stock():
    data = request.get_json()
    # Here I want tu use Bcrypt from flask
    new_stock = Stock(
        symbol=data.get("symbol"),
        name=data.get("name"),
        current_price=float(data.get("current_price")),
    )
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({"message": "Stock created successfully!"}), 201


# get
@stock.route("/stockGet/<int:stock_id>", methods=["GET"])
def get_stock(stock_id):
    stock = Stock.query.filter_by(stock_id=stock_id).one()
    # stock = db.session.get(Stock, stock_id)
    print(stock.stock_id)
    if stock:
        stock_info = {
            "symbol": stock.symbol,
            "name": stock.name,
            "current_price": stock.current_price,
        }
        return jsonify(stock_info), 200
    return jsonify({"error": "Stock not found, invalid uID or no existent stock"}), 401


# Delete
@stock.route("/stockDelete/<int:stock_id>", methods=["DELETE"])
def delete_stock(stock_id):
    stock = db.session.get(Stock, stock_id)
    if not stock:
        return jsonify({"error": "stock not found"}), 400
    if stock.transactions:
        return jsonify(
            {
                "Error": "Cannot delete stock, it is used in transactions",
                "transactions": [t.trans_id for t in stock.transactions],
            }
        )
    db.session.delete(stock)
    db.session.commit()
    return jsonify({"message": "Stock deleted successfully"}), 200


# Alter
@stock.route("/stockUpdate/<int:stock_id>", methods=["PUT"])
def update_stock(stock_id):
    data = request.get_json()
    stock = db.session.get(Stock, stock_id)

    if stock:
        stock.symbol = data.get("symbol", stock.symbol)
        stock.name = data.get("name", stock.name)
        stock.current_price = data.get("current_price", stock.current_price)

        db.session.commit()
        return jsonify({"message": "Stock updated successfully"}), 200

    return jsonify({"error": "Stock not found"}), 404
