from fastapi import APIRouter
from schemas.todolist import Category, CategoryUpdate
from database import create_category, read_categories, update_category

router = APIRouter(tags=["Categorias"])

# Adicionar categoria
@router.post("/", summary="Adicionar categoria")
def create_category_endpoint(category: Category):
    try:
        id = create_category(category.name, category.color)
        return {"message": "Categoria adicionada com sucesso", "category": {"category_id": id, "name": category.name, "color": category.color, "active": 1}}
    except:
        return {"message": "Erro ao adicionar categoria"}
    
# Obter categorias
@router.get("/", summary="Obter categorias")
def read_categories_endpoint():
    return read_categories()

# Atualizar categoria
@router.put("/{category_id}", summary="Atualizar categoria")
def update_category_endpoint(category_id: int, update: CategoryUpdate):
    status = update_category(category_id, update.active)

    if status == "Success":
        return {"message": "Categoria atualizada com sucesso"}
    elif status == "NotFound":
        return {"message": "Categoria não encontrada"}
    else:
        return {"message": "Erro ao atualizar categorias"}