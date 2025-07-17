from datetime import datetime
from dotenv import load_dotenv
from app.db.supabase_client import supabase
from app.services.supabase_getter import check_code_exists, check_locality_exists

load_dotenv()

def login_user(user_name, password): 
    try:
        user_name = user_name.strip()
        password = password.strip()

        response = supabase.rpc("check_user_credentials", {
            "p_user_name": user_name,
            "p_password": password
        }).execute()

        print(f"Response from check_user_credentials: {response}")

        if response.data is True:
            return True
        else:
            return False    
        
    except Exception as e:
        print(f"Error al verificar las credenciales del usuario: {e}")
        return False
    
def register_user(
        user_name: str,
        password: str,
        lat: float | None = None,
        lon: float | None = None,
        city_id: int | None = None,
    ):

    try:
        user_name = user_name.strip()
        password = password.strip()

        # El payload debe usar EXACTAMENTE los nombres de parámetros del RPC
        payload = {
            "p_user_name": user_name,
            "p_lat": lat,
            "p_lon": lon,
            "p_city_id": city_id,
            "p_password": password,
        }

        # Llamada al procedimiento
        response = supabase.rpc("add_user", payload).execute()
        print(f"Response from add_user: {response}")

        # SupabasePy deja el valor retornado en response.data
        # (viene como string o int según versión; lo convertimos a int por claridad)
        if response.data is not None:
            return int(response.data)
        else:
            return None

    except Exception as e:
        print(f"Error al crear el usuario: {e}")
        return None
