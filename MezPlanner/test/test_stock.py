import pytest
from flask import Flask
from backend.blueprints.stock.routes import stock
from backend.blueprints.app import db
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))


@pytest.fixture(scope="session")
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./mezBaseTest.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(stock, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


def test_create_stock(client):
    response = client.post("/stockCreate", json={
        "symbol": "TEST",
        "name": "testStock",
        "current_price": 12.99,
        })
    assert response.status_code == 201
    assert b"Stock created successfully!" in response.data


flag = False
if flag:
    def test_get_stock(client):
        response = client.get("stockGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["symbol"] == "TEST"


    def test_update_stock(client):
        response = client.put("stockUpdate/1", json={
            "symbol": "TEST33"
            })
        assert response.status_code == 200
        assert b"Stock updated successfully" in response.data


    def test_delete_stock(client):
        response = client.delete("/stockdelete/1")
        assert response.status_code == 200
        assert b"Stock deleted successfully" in response.data


    def test_create_stock_safe(client):
        response = client.post("/stockCreate", json={
            "symbol": "TEST",
            "name": "testStock",
            "current_price": "12,99",
            })
        assert response.status_code == 201
        assert b"Stock created successfully!" in response.data

















