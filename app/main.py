from fastapi import FastAPI
from app import crud

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API TODO"}

@app.get("/todos")
def get_todos():
    return crud.get_all_todos()