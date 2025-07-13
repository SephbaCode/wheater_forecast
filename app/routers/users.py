from fastapi import APIRouter
from app.services.user import login_user

router = APIRouter(prefix="", tags=["Usuarios"])


@router.get("/login/")
def login(user_name: str, password: str):
    
    if login_user(user_name, password):
        return {"status": "OK", "mensaje": "Inicio de sesión exitoso"}
    else:
        print('datos: ', user_name, password)
        return {"status": "ERROR", "detalle": "Credenciales incorrectas"}