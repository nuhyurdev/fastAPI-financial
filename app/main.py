# main.py
from typing import List
from fastapi import FastAPI
from uuid import uuid4 
from datetime import datetime
from .models import FinData


app = FastAPI()

db : List[FinData](
    FinData(
    id=uuid4(),
    name="example",
    time=datetime.now(),
    open=1515.55,
    close=515.55,
    high=215.55,
    low=566.55
    )
)
@app.get("/")
async def root():
    return {"message": "Hello from financial API"}

@app.get("/api/v1/findata")
async def get_findata():
    return db