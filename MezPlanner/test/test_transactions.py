import pytest
from flask import Flask
from backend.blueprints.transaction.routes import transaction
from backend.blueprints.transaction.models import Transaction
from backend.blueprints.wallet.models import Wallet
from backend.blueprints.stock.models import Stock
from backend.blueprints.app import db
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from datetime import datetime

@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./mezBaseTest.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(transaction, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


flag = True
if flag:

    def test_create_transaction(client):
        response = client.post("/transactionCreate", json={
            "walet_id": 1,
            "stok_id": 1,
            "qtde": 5,
            "price": 100.5,
            "trans_date": "2025-03-22T12:12:42",
            "trans_type": 1,
            })
        assert b"Transaction created successfully" in response.data
        assert response.status_code == 201

    def test_get_transaction(client):
        response = client.get("/transactionGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["walet_id"] == 1

    def test_update_transaction(client):
        response = client.put("/transactionUpdate/1", json={
            "qtde": 10,
            })
        assert response.status_code == 200
        assert b"Transaction updated successfully" in response.data
    

    def test_delete_transaction(client):
        response = client.delete("/transactionDelete/1")
        assert response.status_code == 200
        assert b"Transaction deleted successfully" in response.data

    def test_create_transaction_safe(client):
        response = client.post("/transactionCreate", json={
            "walet_id": 1,
            "stok_id": 1,
            "qtde": 5,
            "price": 100.5,
            "trans_date": "2025-03-22T12:12:42",
            "trans_type": 1,
            })
        assert b"Transaction created successfully" in response.data
        assert response.status_code == 201
