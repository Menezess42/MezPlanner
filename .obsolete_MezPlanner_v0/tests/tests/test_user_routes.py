# -----------------
# File: File
# Description: Test script for User routes
# Author: Menezess42
# Created: Tue 22-10-2024 15:10
# Last Modified: Tue 22-10-2024 15:10
# -----------------
# from backend.blueprints.user.models import User
import pytest
from backend.blueprints.app import create_app, db
import sys
import os

# Adiciona o caminho do backend ao PYTHONPATH
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
)


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    with app.app_context():
        # db.init_app(app)
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_user(client):
    """Testa a criação de um novo usuário."""
    response = client.post(
        "/user/userCreate",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "birthday": "1990-01-01",
        },
    )
    assert response.status_code == 201
    assert response.get_json() == {"message": "User created successfully!"}

def test_get_user(client):
    """Testa a obtenção de um usuário existente."""
    client.post(
        "/user/userCreate",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "birthday": "1990-01-01",
        },
    )
    response = client.get("/user/userGet/1")
    assert response.status_code == 200
    assert "username" in response.get_json()

def test_login_user(client):
    """Testa o login de um usuário existente."""
    client.post(
        "/user/userCreate",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "birthday": "1990-01-01",
        },
    )
    response = client.get(
        "/user/userLogin", json={"email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "username" in response.get_json()


def test_update_user(client):
    """Testa a atualização de dados de um usuário"""
    client.post(
        "/user/userCreate",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "birthday": "1990-01-01",
        },
    )
    response = client.put(
        "/user/userUpdate/1", json={"username": "testuser", "email": "test@example.com"}
    )
    assert response.status_code == 200
    assert response.get_json() == {"message": "User updated successfully"}


def test_delete_user(client):
    """Testa a exclusão de um usuário."""
    client.post(
        "/user/userCreate",
        json={
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "birthday": "1990-01-01",
        },
    )
    response = client.delete("/user/userDelete/1")
    assert response.status_code == 200
    assert response.get_json() == {"message": "User deleted successfully"}

