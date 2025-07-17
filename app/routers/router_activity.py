from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from app.services.activities import get_activity, insert_activity_with_audit, edit_activity_with_audit
from app.services.routines import register_routine

router = APIRouter(prefix="", tags=["Actividades"])


@router.get("/get_activities/")
def get_activitys():
    response = get_activity()
    
    if response != []:       
        return {"status": "OK", "data": response}
    else:
        return {"status": "ERROR", "detalle": "No se encontraron actividades"}
    
    
@router.post("/create_activity/")
def create_activity(user_name: str, activity_name: str, description: str = ""):
    success = insert_activity_with_audit(user_name, activity_name, description)
    if success == True:
        return {"status": "OK", "message": "Actividad creada y auditada"}
    else:
        return {"status": "ERROR", "message": "No se pudo crear la actividad", "error": str(success)}
    
@router.post("/edit_activity/")
def edit_activity(
    user_name: str, 
    activity_id: int, 
    new_name: str, 
    new_description: Optional[str] = ""
):
    success = edit_activity_with_audit(user_name, activity_id, new_name, new_description)
    if success == True:
        return {"status": "OK", "message": "Actividad editada y auditada"}
    else:
        return {"status": "ERROR", "message": "No se pudo editar la actividad", "error": str(success)}