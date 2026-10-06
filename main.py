from fastapi import FastAPI, HTTPException
from entities.task import Task
from entities.user import User, UserResponse, UserResponseList, UserResponseRaw

import database
import symmetric_encryption


app = FastAPI(title="Python API", version="1.0.0")

database.initialize_database()

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    connection = database.connect()
    try:
        with connection:
            dbresult = connection.execute(
                "SELECT title, description FROM tasks"
            )
            tasks = [
                Task(title=row[0], description=row[1])
                for row in dbresult.fetchall()
            ]
            return tasks
    finally:
        connection.close()


@app.post("/tasks")
def create_task(payload: Task):
    connection = database.connect()
    try:
        with connection:
            connection.execute(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                (payload.title, payload.description),
            )
    finally:
        connection.close()
    return "All done"


@app.post("/users")
def create_user(payload: User):
    connection = database.connect()
    encrypted_cpr = symmetric_encryption.encrypt(payload.cpr_number)
    try:
        with connection:
            connection.execute(
                "INSERT INTO users (username, password, firstname, lastname, cprNumber) VALUES (?, ?, ?, ?, ?)",
                (payload.firstname, payload.password, payload.firstname, payload.lastname, encrypted_cpr),
            )
            connection.commit()
    finally:
        connection.close()
    return "All done"


@app.get("/users", response_model=list[UserResponseList])
def get_users():
    connection = database.connect()
    try:
        with connection:
            
            dbresult = connection.execute(
                "SELECT username, firstname, lastname FROM users"
            )
            users = [
                UserResponseList(username=row[0], firstname=row[1], lastname=row[2])
                for row in dbresult.fetchall()
            ]
            return users
    finally:
        connection.close()



@app.get("/users/{id}", response_model=UserResponseRaw)
def get_user(id: int):
    connection = database.connect()
    try:
        with connection:
            row = connection.execute(
                "SELECT username, firstname, lastname, cprNumber FROM users WHERE id = ?",
                (id,),
            ).fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="User not found")
            return UserResponseRaw(username=row[0], firstname=row[1], lastname=row[2], cpr_number_encrypted=row[3])
    finally:
        connection.close()


@app.post("/encryption")
def encrypt_symmetric(message: str):
    database.connec
    return symmetric_encryption.encrypt(message)
    
