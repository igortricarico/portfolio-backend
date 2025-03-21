from pydantic import BaseModel

class Category(BaseModel):
    name: str
    color: str

class CategoryUpdate(BaseModel):
    active: int
    
class Task(BaseModel):
    description: str
    category_id: int