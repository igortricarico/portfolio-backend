from fastapi import APIRouter
from schemas.todolist import Task

router = APIRouter()
tasks = []

@router.get("/")
def read_tasks():
    return tasks

# Adicionar nova tarefa
@router.post("/")
def create_task(task: Task):
    tasks.append(task)

    return {"message": "Tarefa adicionada"}

# Obter tarefa
@router.get("/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    
    return {"error": "Tarefa não encontrada"}

# Atualizar tarefa
@router.put("/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
        
        
    return {"error": "Tarefa não encontrada"}

# Excluir tarefa
@router.delete("/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return {"message": "Tarefa deletada"}
        
    return {"error": "Tarefa não encontrada"}