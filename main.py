from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}

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
        "developer": "Dev1"
    }