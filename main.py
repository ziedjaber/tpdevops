from fastapi import FastAPI, HTTPException
import socket
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}


def get_local_ip():
    """Récupère l'adresse IP locale de la machine connectée au réseau."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello {name}",
        "developer": "Khaled",  # Remplacez par votre nom ou "Dev2" selon vos consignes
        "hostname": socket.gethostname(),
        "IP": get_local_ip()
    }
    
@app.get("/addition")
def addition(a: int, b: int):
    return {
        "le est result a+b=": a + b,
        "developer": "Dev1"
    }

class DivisionRequest(BaseModel):
    a: float
    b: float


@app.post("/divide")
def divide(data: DivisionRequest):
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )

    return {
        "result a/b=": data.a / data.b,
        "developer": "Dev2"
    }