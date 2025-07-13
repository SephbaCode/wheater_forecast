from datetime import datetime
from dotenv import load_dotenv
from app.db.supabase_client import supabase
from app.services.supabase_getter import check_code_exists, check_locality_exists

load_dotenv()

def save_forecast_to_db(data):
    
    location_id = data["city"]["id"]
    if not check_locality_exists(supabase, location_id):
        print(f"La locación con id {location_id} no existe en la base de datos. -- creando una nueva.")
        # insertando la locacion
        try:
            supabase.rpc("insert_location", {
            "location_id": location_id,
            "name": data["city"]["name"],
            "country": data["city"]["country"],
            "timezone": data["city"]["timezone"],
            "lat": data["city"]["coord"]["lat"],
            "lon": data["city"]["coord"]["lon"]
            }).execute()
        except Exception as e:
            print(f"Error al insertar la locación: {e}")
    else: 
        print(f"La locación con id {location_id} ya existe en la base de datos. -- no es necesario insertar una nueva locación.")
        

    # para cada entrada en el pronóstico
    for entry in data["list"]:
        
        # verificar si el clima existe
        weather = entry.get("weather", [{}])[0]
        weather_id = weather.get("id")


        if weather_id is not None and not check_code_exists(supabase, "check_weather_id_exists", "p_weather_id", weather_id):
            print(f"El clima con id {weather_id} no existe en la base de datos. -- creando un nuevo clima.")
            try:
                supabase.rpc("insert_weather", {
                    "p_weather_id": weather.get("id"),
                    "p_main": weather.get("main"),
                    "p_description": weather.get("description"),
                    "p_icon": weather.get("icon")
                }).execute()
            except Exception as e:
                print(f"Error al insertar el clima: {e}")
        
        try:
            dt = datetime.fromtimestamp(entry["dt"])
            dt_bigint = entry["dt"]
            dt_txt = entry["dt_txt"]

            main = entry["main"]
            wind = entry.get("wind", {})
            clouds = entry.get("clouds", {})
            rain = entry.get("rain", {})
            pop = entry.get("pop", 0.0)

            # Llamada a la función SQL upsert_weather_forecast
            supabase.rpc("upsert_weather_forecast", {
                "p_dt": dt_bigint,
                "p_dt_txt": dt_txt,
                "p_temp": main.get("temp"),
                "p_feels_like": main.get("feels_like"),
                "p_temp_min": main.get("temp_min"),
                "p_temp_max": main.get("temp_max"),
                "p_pressure": main.get("pressure"),
                "p_sea_level": main.get("sea_level"),
                "p_grnd_level": main.get("grnd_level"),
                "p_humidity": main.get("humidity"),
                "p_temp_kf": main.get("temp_kf"),  # puede ser None
                "p_weather_id": weather_id,
                "p_clouds_all": clouds.get("all"),
                "p_wind_speed": wind.get("speed"),
                "p_wind_deg": wind.get("deg"),
                "p_wind_gust": wind.get("gust"),
                "p_visibility": entry.get("visibility"),
                "p_pop": pop,
                "p_rain_3h": rain.get("3h"),
                "p_pod": entry.get("sys", {}).get("pod"),  # 'n' o 'd'
                "p_location": location_id
            }).execute()

        except Exception as e:
            print(f"Error al insertar el pronóstico: {e}")




