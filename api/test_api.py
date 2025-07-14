import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"LarousseIA" in resp.data

def test_prompt_ok(client):
    resp = client.get("/prompt/Cómo cuidar una orquídea?")
    assert resp.status_code == 200
    assert "respuesta" in resp.get_json()

def test_prompt_empty(client):
    resp = client.get("/prompt/   ")
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_guardar_ok(client):
    data = {
        "role": "user",
        "pregunta": "¿Necesita luz directa una suculenta?",
        "respuesta": "No, prefiere luz indirecta brillante."
    }
    resp = client.post("/guardar", json=data)
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_guardar_faltan_campos(client):
    data = {"role": "user", "pregunta": "¿Y la albahaca?"}
    resp = client.post("/guardar", json=data)
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_historial(client):
    resp = client.get("/historial")
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)
