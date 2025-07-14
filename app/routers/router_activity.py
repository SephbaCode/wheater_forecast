from fastapi import APIRouter
from app.services.activitys import get_activity, insert_activity_with_audit

router = APIRouter(prefix="", tags=["Actividades"])


@router.get("/get_activitys/")
def get_activitys():
    response = get_activity()
    
    if response != []:       
        return {"status": "OK", "data": response}
    else:
        return {"status": "ERROR", "detalle": "No se encontraron actividades"}
    
    
@router.post("/activitys/")
def create_activity(user_name: str, activity_name: str, description: str = ""):
    success = insert_activity_with_audit(user_name, activity_name, description)
    if success == True:
        return {"status": "OK", "message": "Actividad creada y auditada"}
    else:
        return {"status": "ERROR", "message": "No se pudo crear la actividad", "error": str(success)}
    