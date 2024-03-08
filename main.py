from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Trabajo Practico 5",
    version="0.0.1"
)

users_db = {}


@app.post("/api/v1/register")
async def register_user(username: str, email: str, password: str):
    # Verificar si el usuario ya existe
    if username in users_db:
        return {"message": "Error: El nombre de usuario ya está registrado"}

    # Almacenar el usuario en el almacén temporal
    users_db[username] = {"username": username,
                          "email": email,
                          "password": password,
                          "status": 200}

    return {"message": "Usuario registrado exitosamente"}


@app.get("/api/v1/user_id")
async def get_user(user_id: str):
     users = {
        "usuario1": {
            "username": "Jera4",
            "name": "Jeralin"
        },
        "id-68": {
            "username": "Caradepanocho18",
            "name": "Ian"

        }

     }

     if user_id in users:
        users = users[user_id]
        return JSONResponse(
            status_code=status.HTTP_200_OK
            , content= users
        )
     else:
        return JSONResponse(
          status_code=status.HTTP_404_NOT_FOUND,
          content="No existe usuario"

        )


app = FastAPI()
task_db = {}

class Task(BaseModel):
    title: str
    description: str
    status: str

@app.post("/tasks/create")
async def create_task(task: Task):
    # Puedes validar más campos según tus necesidades
    task_id = len(task_db) + 1
    task_data = task.dict()
    task_db[task_id] = task_data
    return {"message": "Tarea creada exitosamente"}


app = FastAPI()

users_db = {}
tasks_db = {}

@app.get("/tasks/{user_id}")
async def get_tasks(user_id: str):
    if user_id in tasks_db:
        user_tasks = tasks_db[user_id]
        return {"tasks": user_tasks}
    else:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para el usuario especificado")