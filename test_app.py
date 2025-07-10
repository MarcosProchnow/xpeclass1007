import os
import pytest
from app import app

os.environ["VALID_TOKEN"] = "123456"

VALID_TOKEN = os.getenv("VALID_TOKEN")

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_unauthorized_train_endpoint(client):
    response = client.get('/train')
    assert response.status_code == 401

def test_train_endpoint(client):
    response = client.get('/train?token=123456')
    assert response.status_code == 200

    data = response.get_json()

    # Verifica se a resposta tem as chaves esperadas
    assert "accuracy" in data
    assert "classification_report" in data

    # Verifica se o accuracy é um número
    assert isinstance(data["accuracy"], float)

    # Verifica se o classification_report é um dicionário
    assert isinstance(data["classification_report"], dict)
