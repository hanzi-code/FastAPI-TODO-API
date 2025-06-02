from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
