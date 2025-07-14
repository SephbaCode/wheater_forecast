from fastapi import APIRouter, HTTPException
from typing import Optional

from app.services.user import login_user, register_user

router = APIRouter(prefix="", tags=["Usuarios"])


@router.get("/login/")
def login(user_name: str, password: str):
    
    if login_user(user_name, password):
        return {"status": "OK", "mensaje": "Inicio de sesión exitoso"}
    else:
        print('datos: ', user_name, password)
        return {"status": "ERROR", "detalle": "Credenciales incorrectas"}
    
    
@router.post("/register-query/")
def register_query(
    user_name: str,
    password: str,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    city_id: Optional[int] = None,
):
    user_id = register_user(user_name, password, lat, lon, city_id)

    if user_id:
        return {"status": "OK", "mensaje": "Usuario creado", "user_id": user_id}
    else:
        raise HTTPException(status_code=400, detail="No se pudo crear el usuario")