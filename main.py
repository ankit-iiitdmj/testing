from fastapi import FastAPI
from pydantic import BaseModel
import time
import asyncio

app = FastAPI()

def addi(var):
    for i in range(100000000):
        var = var +2
        var = var -1
    return var

@app.get("/")
def index(var:int):
    result = addi(var)
    return {'msg': result}
