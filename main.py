"""API FastAPI pour les opérations arithmétiques et la gestion d'items."""

import socket
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    """Retourne un message indiquant que l'API fonctionne."""
    return {"message": "it works !"}


def get_local_ip():
    """Récupère l'adresse IP locale de la machine connectée au réseau."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("10.255.255.255", 1))
        ip_address = sock.getsockname()[0]
    except OSError:
        ip_address = "127.0.0.1"
    finally:
        sock.close()
    return ip_address


@app.get("/greeting")
def greeting(name: str):
    """Retourne un message d'accueil avec le nom d'hôte et l'adresse IP locale."""
    return {
        "message": f"Hello {name}",
        "developer": "Khaled",
        "hostname": socket.gethostname(),
        "IP": get_local_ip(),
    }


@app.get("/addition")
def addition(a: int, b: int):
    """Retourne la somme de deux entiers."""
    return {
        "le est result a+b=": a + b,
        "developer": "Dev1",
    }


@app.get("/soustraction")
def soustraction(a: int, b: int):
    """Retourne la différence entre deux entiers."""
    return {
        "result a-b=": a - b,
        "developer": "Dev1",
    }


class DivisionRequest(BaseModel):
    """Modèle de requête pour la division."""

    a: float
    b: float


@app.post("/divide")
def divide(data: DivisionRequest):
    """Retourne le quotient de deux nombres flottants."""
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed",
        )

    return {
        "result a/b=": data.a / data.b,
        "developer": "Dev2",
    }


class Numbers(BaseModel):
    """Modèle de requête pour la multiplication."""

    a: float
    b: float


@app.post("/multiply")
def multiply_numbers(nums: Numbers):
    """Retourne le produit de deux nombres flottants."""
    result = nums.a * nums.b
    return {
        "result a*b=": result,
        "developer": "Leader",
    }


items = {
    1: {"name": "Computer", "price": 1200},
    2: {"name": "Keyboard", "price": 50},
    3: {"name": "Mouse", "price": 25},
}


class ItemUpdate(BaseModel):
    """Modèle de mise à jour d'un item."""

    name: str
    price: float


@app.put("/update/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    """Met à jour un item existant selon son identifiant."""
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    items[item_id] = {
        "name": item.name,
        "price": item.price,
    }

    return {
        "message": "Item updated successfully",
        "id": item_id,
        "item": items[item_id],
        "developer": "Dev2",
    }


@app.delete("/remove/{item_id}")
def remove_item(item_id: int):
    """Supprime un item existant selon son identifiant."""
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    deleted_item = items.pop(item_id)

    return {
        "message": f"Item with id {item_id} has been successfully deleted",
        "deleted_item": deleted_item,
        "developer": "Dev1",
    }
