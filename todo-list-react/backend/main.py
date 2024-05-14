from fastapi import HTTPException, FastAPI, Response, Depends
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List, Dict
# import mysql.connector
# from database import get_database_connection

# run this in order
# ./venv/Scripts/activate
# uvicorn main:app --reload
# or 
# python -m uvicorn main:app --reload



app = FastAPI()

# class User(BaseModel):
#     name: str
#     email: str

# # Database
# def get_database_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="PassAsOne",
#         database="mydatabase"
#     )

# @app.get("/")
# async def root():
#     return{"messege": "Hello, World!"}

# @app.post("/users")
# async def create_user(user: User):
#     connection = get_database_connection()
#     cursor = connection.cursor()
#     query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#     values = (user.name, user.email)
#     cursor.execute(query, values)
#     connection.commit()
#     connection.close()
#     return {"message": "User created successfully"}

# @app.get("/users")
# async def read_users():
#     connection = get_database_connection()
#     cursor = connection.cursor()
#     query = "SELECT * FROM users"
#     cursor.execute(query)
#     users = cursor.fetchall()
#     connection.close()
#     return users


# The Not Database

tasks = []
accounts = []

class TaskSchema(BaseModel):
    id: int
    task_name: str
    task_description: str
    is_completed: bool = False

class UpdateTask(BaseModel):
    id: Optional[int] = None
    task_name: Optional[str] = None
    task_description: Optional[str] = None
    is_completed: Optional[bool] = None

class AccountSchema(BaseModel):
    id: int
    name: str
    password: str

# Cookies
# fetching login id
@app.get("/login")
async def login(password: str):
    for account in accounts:
        if account.password == password:
            return account


# make account
@app.post("/login/register")
async def register(account: AccountSchema):
    accounts.append(account)
    return {"success": True, "message": f"successfully created user {account}"}


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