from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict


# run this in order
# ./venv/Scripts/activate
# uvicorn main:app --reload

app = FastAPI()

tasks = []

class TaskSchema(BaseModel):
    id: int
    task_name: str
    is_completed: bool = False

class UpdateTask(BaseModel):
    id: Optional[int] = None
    task_name: Optional[str] = None
    is_completed: Optional[bool] = None

# todo methods
@app.get("/tasks")
def get_tasks():
    return tasks

# fetching the task
@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    for task in tasks:
        if task.id == id:
            return task
        

# post new task
@app.post("/tasks/new")
def create_task(task: TaskSchema):
    tasks.append(task)
    return {"success": True, "message": "successfully created task"}

# Updates task
@app.put("/todos/{id}")
def update_task(id: int, new_task: UpdateTask):
    for index, task in enumerate(tasks):
        if task.id == id:
            tasks[index] = new_task
            tasks[index].id = id
            return {"success": True, "message": "successfully edited task"}

# Deletes task
@app.delete("/tasks/{id}")
def delete_task(id: int):
    for index, task in enumerate(tasks):
        if task.id == id:
            del tasks[index]
            return {"msg":"todo has been deleted successfully"}