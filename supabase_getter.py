import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from supabase_client import supabase

load_dotenv()

def get_locations_codes():
    try:
        result = supabase.rpc("get_all_id_w").execute()
        print("Códigos de localizaciones obtenidos:", result.data)
        return result.data
    except Exception as e:
        print("Error al obtener códigos de localizaciones:", e)
        return []

