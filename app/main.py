from fastapi import FastAPI
from app.routers.users import router as user_router   

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Planificador Climático")
app.include_router(user_router, prefix="/usuarios", tags=["Usuarios"])       
# Middleware CORS (si planeas consumir desde frontend)

# Ruta base
@app.get("/")
def root():
    return {"mensaje": "API del planificador climático activa"}
