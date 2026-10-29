from fastapi import FastAPI
from pydantic import BaseModel
import socket

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
@app.get("/addition")
def addition(a: int, b: int):
    return {
        "le est result a+b=": a + b,
        "developer": "Dev1"
    }

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/multiply")
def multiply_numbers(nums: Numbers):
    result = nums.a * nums.b
    return {
        "result a*b=": result,
        "developer": "Leader"
    }