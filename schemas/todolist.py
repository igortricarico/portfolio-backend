from pydantic import BaseModel

class Task(BaseModel):
    id: int
    description: str
    category: str