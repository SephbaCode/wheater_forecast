from fastapi import FastAPI
from app.routers.weather import router as weather_router
from app.routers.users import router as user_router
from app.routers.router_activity import router as activity_router
from app.routers.router_routine import router as routine_router
from app.routers.router_recommendation import router as recommendation_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Planificador Climático")
app.include_router(weather_router, prefix="/clima", tags=["Clima"])
app.include_router(user_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(activity_router, prefix="/actividades", tags=["Actividades"])   
app.include_router(routine_router, prefix="/rutinas", tags=["Rutinas"])  
app.include_router(recommendation_router, prefix="/recomendaciones", tags=["Recomendaciones"])  

# Ruta base
@app.get("/")
def root():
    return {"mensaje": "API del planificador climático activa"}
