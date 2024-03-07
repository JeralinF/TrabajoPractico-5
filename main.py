from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

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
