import pytest
from flask import Flask
from backend.blueprints.task.routes import task
from backend.blueprints.task.models import Task
from backend.blueprints.app import db
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

@pytest.fixture
def app():
    """Configura um app Flask de teste."""
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(task, url_prefix="/")

    with app.app_context():
        db.create_all()
    
    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """Cria um cliente de teste para fazer requisições."""
    return app.test_client()


def test_create_task(client):
    """Testa a criação de uma task."""
    response = client.post("/taskCreate", json={
        "name": "Nova Tarefa",
        "description": "Descrição de teste",
        "color": "azul",
        "template": "template1",
        "weekdays": 5,
        "usr_id": 1
    })

    assert response.status_code == 201
    assert b"Stock created successfully" in response.data


def test_get_task(client):
    """Testa a recuperação de uma task."""
    client.post("/taskCreate", json={
        "name": "Tarefa Exemplo",
        "description": "Descrição Exemplo",
        "color": "vermelho",
        "template": "template2",
        "weekdays": 3,
        "usr_id": 2
    })

    response = client.get("/taskGet/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Tarefa Exemplo"


def test_update_task(client):
    """Testa a atualização de uma task."""
    client.post("/taskCreate", json={
        "name": "Tarefa Antiga",
        "description": "Descrição Antiga",
        "color": "verde",
        "template": "template3",
        "weekdays": 2,
        "usr_id": 3
    })

    response = client.put("/taskUpdate/1", json={
        "name": "Tarefa Atualizada"
    })
    assert response.status_code == 200
    assert b"Task updated successfully" in response.data


def test_delete_task(client):
    """Testa a exclusão de uma task."""
    client.post("/taskCreate", json={
        "name": "Tarefa a Deletar",
        "description": "Para teste",
        "color": "cinza",
        "template": "template4",
        "weekdays": 7,
        "usr_id": 4
    })

    response = client.delete("/taskDelete/1")
    assert response.status_code == 200
    assert b"Task deleted successfully" in response.data
