import pytest
from flask import Flask
from backend.blueprints.user.routes import user
from backend.blueprints.user.models import User
from backend.blueprints.task.models import Task
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
    app.register_blueprint(user, url_prefix="/")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_user(client):
    response = client.post("/userCreate", json={
        "name": "User test 2",
        "email": "ariel@test.com",
        "password": "ariel",
        "birthday": "2025-01-06",
        })
    assert response.status_code == 201
    assert b"User created successfully!" in response.data


def test_get_user(client):
    response = client.get("/userGet/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["email"] == "ariel@test.com"


def test_update_user(client):
    response = client.put("userUpdate/1", json={
        "name": "User updated-Get test"
        })
    assert response.status_code == 200
    assert b"User updated successfully" in response.data


def test_login_user(client):
    response = client.post("/userLogin", json={
        "email": "ariel@test.com",
        "password": "ariel",
       })
    assert response.status_code == 200
    data = response.get_json()
    assert data["email"] == "ariel@test.com"


def test_delete_user(client):
    response = client.delete("/userDelete/1")
    assert response.status_code == 200
    assert b"User deleted successfully" in response.data


def test_create_user_safe(client):
    response = client.post("/userCreate", json={
        "name": "User test 2",
        "email": "ariel@test.com",
        "password": "ariel",
        "birthday": "2025-01-06",
        })
    assert response.status_code == 201
    assert b"User created successfully!" in response.data

