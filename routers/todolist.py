from fastapi import APIRouter
from schemas.todolist import Task
from database import create_task, read_tasks, delete_task

router = APIRouter(tags=["Tarefas"])

# Adicionar tarefa
@router.post("/", summary="Adicionar tarefa")
def create_task_endpoint(task: Task):
    try:
        id = create_task(task.description, task.category_id)
        return {"message": "Tarefa adicionada com sucesso", "task": {"task_id": id, "description": task.description, "category_id": task.category_id}}
    except:    
        return {"message": "Erro ao adicionar tarefa"}
    
# Obter tarefas
@router.get("/", summary="Obter tarefas")
def read_tasks_endpoint():
    return read_tasks()

# Excluir tarefa
@router.delete("/{task_id}", summary="Excluir tarefa")
def delete_task_endpoint(task_id: int):
    if delete_task(task_id):
        return {"message": "Tarefa deletada com sucesso"}
    
    return {"message": "Tarefa não encontrada"}