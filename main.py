from fastapi import FastAPI
from supabase_getter import get_locations_codes
from weather_fetcher import fetch_weather_forecast, fetch_weather_forecast_by_city_id
from supabase_upper import save_forecast_to_db, check_locality_exists

app = FastAPI()

# Ubicación por defecto (puedes ampliarlo a varias)
DEFAULT_LAT = -2.9
DEFAULT_LON = -78.99

@app.get("/")
def root():
    return {"mensaje": "API del planificador climático activa"}

@app.post("/actualizar_clima/")
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



@app.get("/clima_pronostico/")
def clima_pronostico(city_id: int = 3654157):
    try:
        datos = fetch_weather_forecast_by_city_id(city_id)
        return {"status": "OK", "datos": datos}
    except Exception as e:
        return {"status": "ERROR", "detalle": str(e)}
    

    