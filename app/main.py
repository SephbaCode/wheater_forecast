from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.router_activity import router as activity_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Planificador Climático")
app.include_router(user_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(activity_router, prefix="/actividades", tags=["Actividades"])       

# Ruta base
@app.get("/")
def root():
    return {"mensaje": "API del planificador climático activa"}
