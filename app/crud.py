from sqlalchemy.orm import Session
from . import models, schemas

def get_all_todos():
    return db.query(models.Todo).all()

def create_todos(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db_todo.completed = False
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo