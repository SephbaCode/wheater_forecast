from datetime import datetime
from dotenv import load_dotenv
from app.db.supabase_client import supabase
from app.services.supabase_getter import check_code_exists, check_locality_exists

load_dotenv()

""" Payload de ejemplo
    payload = {
    "p_user_name": "juanperez",
    "p_user_act": 42,
    "p_estatus": "SUGERIDA",
    "p_message": "Recomendado correr al atardecer",
    "p_weather_id": 12,
    "p_date": datetime.now() + timedelta(days=1)  # por ejemplo, mañana
}
"""

def register_recommendation(
        user_name: str,
        user_act: int,
        estatus: str,
        message: str,
        weather_id: int,
        date: datetime | None = None
    ):
    try:
        user_name = user_name.strip()

        # El payload debe usar EXACTAMENTE los nombres de parámetros del RPC
        payload = {
            "p_user_name": user_name,
            "p_user_act": user_act,
            "p_estatus": estatus,
            "p_message": message,
            "p_weather_id": weather_id,
            "p_date": date
        }

        # Llamada al procedimiento
        response = supabase.rpc("add_user_recommendation", payload).execute()
        print(f"Response from add_user_recommendation: {response}")

        # SupabasePy deja el valor retornado en response.data
        if response.data is not None:
            return int(response.data)
        else:
            return None

    except Exception as e:
        print(f"Error al registrar la recomendación para el usuario: {e}")
        return e
    
def get_recommendations_by_user(user_name: str):
    try:
        user_name = user_name.strip()

        # Llamada al procedimiento
        response = supabase.rpc("get_user_recommendations", {"p_user_name": user_name}).execute()
        print(f"Response from get_recommendations_by_user: {response}")

        if response.data is not None:
            return response.data
        else:
            return []

    except Exception as e:
        print(f"Error al obtener las recomendaciones del usuario: {e}")
        return e