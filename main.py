from fastapi import FastAPI
from routers import todolist
from pydantic import BaseModel

app = FastAPI()

app.include_router(todolist.router, prefix="/tasks")

# Rota Padrão

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API"}