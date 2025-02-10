import pytest
from flask import Flask
from backend.blueprints.task_time.routes import task_time
from backend.blueprints.task_time.models import Task_time
from backend.blueprints.task.models import Task
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
    app.register_blueprint(task_time, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()



flag = True
if flag:
    def test_create_taskTime(client):
        response = client.post("/tasktimeCreate", json={
            "startime": "08:00:00",
            "endtime": "10:00:00",
            "tsk_id": 1
        })
        assert response.status_code == 201
        assert b"Task_time created successfully" in response.data



    def test_get_taskTime(client):
        response = client.get("/TaskTimeGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["tsk_id"] == 1

    def test_update_taskTime(client):
        response = client.put("/TaskTimeUpdate/1", json={
            "startime": "06:00:00",
            "endtime": "11:00:00",
        })
        print(response.json)  # <-- Adicione esta linha para ver a resposta do servidor
        assert response.status_code == 200
    


    def test_delete_taskTime(client):
        response = client.delete("/tasktimeDelete/1")
        assert response.status_code == 200
        assert b"Task_time deleted successfully" in response.data


    def test_create_taskTime_sasfe(client):
        response = client.post("/tasktimeCreate", json={
            "startime": "08:00:00",
            "endtime": "10:00:00",
            "tsk_id": 1
        })
        assert response.status_code == 201
        assert b"Task_time created successfully" in response.data

