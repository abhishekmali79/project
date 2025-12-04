from fastapi import FastAPI
from pydantic import BaseModel
import re
from myapp.logic import calculate

#hsxg zmkf suvy jrxb
app=FastAPI()

class inputData(BaseModel):
    name:str
    debt:str
    items:str
    paid:str

@app.get("/")
def home():
    from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI is working!"}

@app.post("/calculate")
def calculate_endpoint(data:inputData):
    result=calculate(data.name,data.debt,data.items,data.paid)
    return {"result": result}