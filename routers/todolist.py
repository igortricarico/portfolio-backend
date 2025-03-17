from fastapi import APIRouter
from schemas.todolist import Task

router = APIRouter()
tasks = []

# Obter tarefas
@router.get("/")
def read_tasks():
    return tasks

# Adicionar tarefa
@router.post("/")
def create_task(task: Task):
    tasks.append(task)

    return {"message": "Tarefa adicionada"}

# Excluir tarefa
@router.delete("/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return {"message": "Tarefa deletada"}
        
    return {"error": "Tarefa não encontrada"}