import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from supabase_client import supabase

load_dotenv()

OW_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather_forecast(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={OW_API_KEY}&lang=es"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_weather_forecast_by_city_id(city_id):
    url = f"https://api.openweathermap.org/data/2.5/forecast?id={city_id}&units=metric&appid={OW_API_KEY}&lang=es"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

