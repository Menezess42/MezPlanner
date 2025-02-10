import pytest
from flask import Flask
from backend.blueprints.task.routes import task
from backend.blueprints.task.models import Task
from backend.blueprints.user.models import User
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
    app.register_blueprint(task, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


flag =True
if flag:
    def test_create_task(client):
        response = client.post("/taskCreate", json={
            "name": "Task Test",
            "description": "This is a test to see if task create is ok",
            "color": "#ffffff",
            "template": 1,
            "weekdays": 1000001,
            "usr_id": 1,
            })
        assert response.status_code == 201
        assert b"Task created successfully" in response.data

    def test_get_task(client):
        response = client.get("/taskGet/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["usr_id"] == 1

    def test_update_task(client):
        response = client.put("/taskUpdate/1", json={
            "description": "Description changed in update task",
            })
        assert response.status_code == 200
        assert b"Task updated successfully" in response.data

    
    def test_delete_task(client):
        response = client.delete("/taskDelete/1")
        assert response.status_code == 200
        assert b"Task deleted successfully" in response.data

    def test_create_task_safe(client):
        response = client.post("/taskCreate", json={
            "name": "Task Test",
            "description": "This is a test to see if task create is ok",
            "color": "#ffffff",
            "template": 1,
            "weekdays": 1000001,
            "usr_id": 1,
            })
        assert response.status_code == 201
        assert b"Task created successfully" in response.data

