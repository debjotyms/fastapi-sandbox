from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"message":"Hello World!"}


@app.get('/about')
def root():
    return {"message":"I am Debjoty!"}