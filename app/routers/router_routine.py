from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from app.services.routines import register_routine, get_routines_by_user

router = APIRouter(prefix="", tags=["Rutinas"])


@router.post("/user_routine/")
def create_user_routine(
    user_name: str,
    activity_id: int,
    date_input: Optional [datetime] | None = None,
    temp_min: Optional [float] | None = None,
    temp_max: Optional [float] | None = None,
    humity: Optional [int] | None = None
):
    response = register_routine(
        user_name, 
        activity_id, 
        date_input, 
        temp_min, 
        temp_max, 
        humity
    )
    
    if isinstance(response, int):
        return {"status": "OK", "message": "Actividad del usuario registrada", "id": response}
    else:
        return {"status": "ERROR", "message": "No se pudo registrar la actividad del usuario", "error": str(response)}
    
@router.get("/user_routines/{user_name}")
def get_user_routines(user_name: str):
    response = get_routines_by_user(user_name)
    
    if isinstance(response, list):
        return {"status": "OK", "message": "Rutinas del usuario obtenidas", "data": response}
    else:
        return {"status": "ERROR", "message": "No se pudieron obtener las rutinas del usuario", "error": str(response)}
