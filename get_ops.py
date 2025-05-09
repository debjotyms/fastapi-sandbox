from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root(name:str = "World"):
    return f"Hello, {name}!"