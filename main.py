from fastapi import FastAPI
from routers import todolist
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(todolist.router, prefix="/tasks")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

# Rota Padrão
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API"}