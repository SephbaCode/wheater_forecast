from datetime import datetime
from typing import Optional
from dotenv import load_dotenv
from app.db.supabase_client import supabase
from app.services.supabase_getter import check_code_exists, check_locality_exists

load_dotenv()

def register_routine(
        user_name: str,
        activity_id: int,
        date_input: datetime | None = None,
        temp_min: float | None = None,
        temp_max: float | None = None,
        humity: int | None = None,
    ):

    try:
        user_name = user_name.strip()

        # El payload debe usar EXACTAMENTE los nombres de parámetros del RPC
        payload = {
            "p_user_name": user_name,
            "p_activity_id": activity_id,
            "p_date_input": date_input,
            "p_temp_min": temp_min,
            "p_temp_max": temp_max,
            "p_humity": humity,
        }

        # Llamada al procedimiento
        response = supabase.rpc("add_user_activity", payload).execute()
        print(f"Response from add_user: {response}")

        # SupabasePy deja el valor retornado en response.data
        # (viene como string o int según versión; lo convertimos a int por claridad)
        if response.data is not None:
            return int(response.data)
        else:
            return None

    except Exception as e:
        print(f"Error al registrar la actividad para el usuario: {e}")
        return e


def get_routines_by_user(user_name: str):
    try:
        user_name = user_name.strip()

        # Llamada al procedimiento
        response = supabase.rpc("get_user_routines", {"p_user_name": user_name}).execute()
        print(f"Response from get_routines_by_user: {response}")

        if response.data is not None:
            return response.data
        else:
            return []

    except Exception as e:
        print(f"Error al obtener las rutinas del usuario: {e}")
        return e