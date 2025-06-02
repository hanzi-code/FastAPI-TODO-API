from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API TODO"}

@app.get("/todos", response_model = list[schemas.TodoOut])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_all_todos(db)

@app.post("/todos", response_model = schemas.TodoOut, status_code = 201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@app.put("/todos/{todo_id}", response_model = schemas.TodoOut)
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code = 404, detail = "TODO não encontrado")
    return todo

@app.delete("/todos/{todo_id}", response_model = schemas.TodoOut)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code = 404, detail = "TODO não encontrado")
    return todo