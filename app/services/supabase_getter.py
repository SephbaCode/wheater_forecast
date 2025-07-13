import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from app.db.supabase_client import supabase

load_dotenv()

def get_locations_codes():
    try:
        result = supabase.rpc("get_all_id_w").execute()
        print("Códigos de localizaciones obtenidos:", result.data)
        return result.data
    except Exception as e:
        print("Error al obtener códigos de localizaciones:", e)
        return []

def check_locality_exists(supabase, location_id: int) -> bool:
    try:
        result = supabase.rpc("check_locality_exists", {"locality_id": location_id}).execute()
        # El valor booleano estará en result.data, por ejemplo: [True]
        if result.data:
            return True
        return False
    except Exception as e:
        print("Error al verificar existencia de localidad:", e)
        return False
    
def check_code_exists(supabase, function, code_name, code: int) -> bool:
    try:
        result = supabase.rpc(function, {code_name: code}).execute()
        # El valor booleano estará en result.data, por ejemplo: [True]
        if result.data:
            return True
        return False
    except Exception as e:
        print(f"Error al verificar existencia de código {code} en la funcion {function}:", e)
        return False

      
