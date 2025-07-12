from fastapi import FastAPI
from app.routers.weather import router as weather_router   #  ← importa tu router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Planificador Climático")
app.include_router(weather_router)       
# Middleware CORS (si planeas consumir desde frontend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción, reemplaza con tu dominio frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ruta base
@app.get("/")
def root():
    return {"mensaje": "API del planificador climático activa"}
