from .models import todos
from .schemas import Todo, TodoCreate

def get_all_todos():
    return todos

def create_todos(todo_data: TodoCreate):
    new_id = max(todo["id"] for todo in todos) + 1 if todos else 1
    new_todo = {"id": new_id, "title": todo_data.title, "completed": False}
    todos.append(new_todo)
    return new_todo

def update_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            return todo
    return None

def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo[id] == todo_id:
            return todos.pop(i)
    return None