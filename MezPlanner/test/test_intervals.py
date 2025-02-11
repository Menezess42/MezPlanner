import pytest
from flask import Flask
from backend.blueprints.interval.routes import intervals
from backend.blueprints.interval.models import Interval
from backend.blueprints.user.models import User
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
    app.register_blueprint(intervals, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


flag = True
if flag:
    def test_create_intervals(client):
        response = client.post("/intervalCreate", json={
            "intvl_type": "df",  # Alterado de "intvl_type" para "type"
            "weekdays": 1010000,  # Exemplo: Segunda e Quarta ativadas
            "valid_startdate": "2025-02-01",
            "valid_endate": "2025-02-10",
            "usr_id": 1
        })
        assert response.status_code == 201
        assert b"Interval created successfully" in response.data

    def test_get_intervals(client):
        response = client.get("/intervalGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["intvl_type"] == "df"

    def test_update_intervals(client):
        response = client.put("/intervalUpdate/1", json={
            "intvl_type": "cd",
        })
        print(response.json)  # <-- Adicione esta linha para ver a resposta do servidor
        assert response.status_code == 200

    def test_delete_intervals(client):
        response = client.delete("/intervalDelete/1")
        assert response.status_code == 200
        assert b"Interval deleted successfully" in response.data

    def test_create_intervals_safe(client):
        response = client.post("/intervalCreate", json={
            "intvl_type": "df",  # Alterado de "intvl_type" para "type"
            "weekdays": 1010000,  # Exemplo: Segunda e Quarta ativadas
            "valid_startdate": "2025-02-01",
            "valid_endate": "2025-02-10",
            "usr_id": 1
        })
        assert response.status_code == 201
        assert b"Interval created successfully" in response.data

