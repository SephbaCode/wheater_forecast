from fastapi import APIRouter
from app.services.supabase_getter import get_locations_codes
from app.services.weather_fetcher import fetch_weather_forecast_by_city_id
from app.services.supabase_upper import save_forecast_to_db

router = APIRouter(prefix="", tags=["Clima"])

@router.post("/actualizar_clima/")
def actualizar_clima():
    try:
        locations = get_locations_codes()
        if not locations:
            return {"status": "ERROR", "detalle": "No se encontraron códigos de localizaciones."}
        
        for location in locations:
            datos = fetch_weather_forecast_by_city_id(location["id_w"])
            save_forecast_to_db(datos)
            print("Pronóstico del clima actualizado correctamente para ", location["id_w"])
            
        return {"status": "OK", "mensaje": "Pronóstico actualizado"}
    except Exception as e:
        return {"status": "ERROR", "detalle": str(e)}

@router.get("/clima_pronostico/")
def clima_pronostico(city_id: int = 3654157):
    try:
        datos = fetch_weather_forecast_by_city_id(city_id)
        return {"status": "OK", "datos": datos}
    except Exception as e:
        return {"status": "ERROR", "detalle": str(e)}
