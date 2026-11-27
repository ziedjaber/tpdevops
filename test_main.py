"""Tests unitaires et de couverture pour l'API FastAPI."""

from fastapi.testclient import TestClient
from main import app

CLIENT = TestClient(app)


def test_read_root():
    """Vérifie la route racine."""
    response = CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_greeting():
    """Vérifie la route greeting."""
    response = CLIENT.get("/greeting", params={"name": "Zied"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello Zied"
    assert "IP" in data


def test_addition():
    """Vérifie la route addition."""
    response = CLIENT.get("/addition", params={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json()["le est result a+b="] == 7


def test_soustraction():
    """Vérifie la route soustraction."""
    response = CLIENT.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json()["result a-b="] == 6


def test_divide_success():
    """Vérifie la division nominale."""
    response = CLIENT.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json()["result a/b="] == 5.0


def test_divide_by_zero():
    """Vérifie le rejet de la division par zéro."""
    response = CLIENT.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400


def test_multiply():
    """Vérifie la multiplication."""
    response = CLIENT.post("/multiply", json={"a": 3, "b": 5})
    assert response.status_code == 200
    assert response.json()["result a*b="] == 15.0


def test_update_and_remove_item():
    """Vérifie la mise à jour puis la suppression d'un item existant."""
    update_resp = CLIENT.put(
        "/update/2",
        json={"name": "Mechanical Keyboard", "price": 90},
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["item"]["name"] == "Mechanical Keyboard"

    remove_resp = CLIENT.delete("/remove/2")
    assert remove_resp.status_code == 200
    assert remove_resp.json()["deleted_item"]["name"] == "Mechanical Keyboard"


def test_update_and_remove_not_found():
    """Vérifie les erreurs 404 pour un id inexistant."""
    assert (
        CLIENT.put("/update/999", json={"name": "Ghost", "price": 1}).status_code
        == 404
    )
    assert CLIENT.delete("/remove/999").status_code == 404
