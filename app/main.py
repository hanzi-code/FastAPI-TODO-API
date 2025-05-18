from fastapi import FastAPI, HTTPException
from . import crud
from .schemas import TodoCreate, Todo


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API TODO"}

@app.get("/todos", response_model = list[Todo])
def get_todos():
    return crud.get_all_todos()

@app.post("/todos", response_model = Todo, status_code = 201)
def create_todo(todo: TodoCreate):
    return crud.create_todo(todo)

@app.put("/todos/{todo_id}", response_model = Todo)
def complete_todo(todo_id: int):
    updated = crud.update_todo(todo_id)
    if not updated:
        raise HTTPException(status_code = 404, detail = "TODO não encontrado")
    return updated

@app.delete("/todos/{todo_id}", response_model = Todo)
def delete_todo(todo_id: int):
    deleted = crud.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code = 404, detail = "TODO não encontrado")
    return deleted