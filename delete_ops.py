from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items = {
    "banana": "an yellow fruit",
    "apple": "a red fruit"
}

@app.get("/items")
def root(name: str = "banana"):
    return items[name]