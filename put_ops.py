from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    description: str

# This is acting like a fake database
# In real life scenario, we will be using our database enpoints
# To keep everything simple, we are using a dictionary here to simulate a real life scenario
items = {
    "bananas": "Yellow fruit.",
    "apples": "Red or green fruit.",
    "oranges": "Orange citrus fruit.",
    "strawberries": "Red berries.",
    "grapes": "Small, sweet fruit growing in clusters."
}

app = FastAPI()

@app.get("/items")
def root(name : str = "bananas"):
    return items[name]  

@app.put("/items")
def update_item(item: Item):
    name = item.name
    items[name] = item.description
    return item