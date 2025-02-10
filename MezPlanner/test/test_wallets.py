import pytest
from flask import Flask
from backend.blueprints.wallet.routes import wallet
from backend.blueprints.wallet.models import Wallet
from backend.blueprints.user.models import User
from backend.blueprints.transaction.models import Transaction
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
    app.register_blueprint(wallet, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


flag =True 
if flag:
    def test_create_wallet(client):
        response = client.post("/walletCreate", json={
            "name": "Test W Name",
            "current_value": "1000.50",
            "highest_value": "2000.50",
            "highest_value_day": datetime.now().isoformat(timespec="seconds"),
            "stock_value": "500.25",
            "own_money_value": "500.25", 
            "credit": "1.5",
            "only_stock_value": "1.5",
            "usr_id":"1",
            })
        assert response.status_code == 201
        assert b"Wallet created successfully!" in response.data



    def test_get_wallet(client):
        response = client.get("/walletGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["usr_id"] == 1

    def test_update_wallet(client):
        response = client.put("/walletUpdate/1", json={
            "name": "Test W Name Updated",
            })
        assert response.status_code == 200
        assert b"Wallet updated successfully" in response.data
    

    def test_delete_wallet(client):
        response = client.delete("/walletDelete/1")
        assert response.status_code == 200
        assert b"Wallet deleted successfully" in response.data


    def test_create_wallet_safe(client):
        response = client.post("/walletCreate", json={
            "name": "Test W Name",
            "current_value": "1000.50",
            "highest_value": "2000.50",
            "highest_value_day": datetime.now().isoformat(timespec="seconds"),
            "stock_value": "500.25",
            "own_money_value": "500.25", 
            "credit": "1.5",
            "only_stock_value": "1.5",
            "usr_id":"1",
            })
        assert response.status_code == 201
        assert b"Wallet created successfully!" in response.data
