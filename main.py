from fastapi import FastAPI
from routers import todolist, category
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(todolist.router, prefix="/tasks")
app.include_router(category.router, prefix="/categories")

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