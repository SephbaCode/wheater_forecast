from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from app.services.recomendation import register_recommendation, get_recommendations_by_user

router = APIRouter(prefix="", tags=["Recomendaciones"])

@router.post("/user_recommendation/")
def create_user_recommendation(
    user_name: str,
    user_act: int,
    estatus: str,
    message: str,
    weather_id: Optional[int] | None = None,
    date: Optional[datetime] | None = None
):
    response = register_recommendation(
        user_name, 
        user_act, 
        estatus, 
        message, 
        weather_id, 
        date
    )
    
    if isinstance(response, int):
        return {"status": "OK", "message": "Recomendación del usuario registrada", "id": response}
    else:
        return {"status": "ERROR", "message": "No se pudo registrar la recomendación del usuario", "error": str(response)}
    
@router.get("/user_recommendations/{user_name}")
def get_user_recommendations(user_name: str):
    response = get_recommendations_by_user(user_name)
    
    if isinstance(response, list):
        return {"status": "OK", "message": "Recomendaciones del usuario obtenidas"}
    else:
        return {"status": "ERROR", "message": "No se pudieron obtener las recomendaciones del usuario", "error": str(response)}