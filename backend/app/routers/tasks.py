from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import Task, TaskCreate
from ..models import tasks_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[Task])
def get_tasks():
    return tasks_db

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks_db) + 1, **task.dict())
    tasks_db.append(new_task)
    return new_task

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            tasks_db.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")