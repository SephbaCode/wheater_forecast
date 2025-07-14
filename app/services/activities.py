from datetime import datetime
from dotenv import load_dotenv
from app.db.supabase_client import supabase
from app.services.supabase_getter import check_code_exists, check_locality_exists

load_dotenv()

def get_activity():
    try:
        response = supabase.rpc("get_activities").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Error al obtener las actividades: {e}")
        return []
    

def insert_activity_with_audit(user_name: str, activity_name: str, description: str) -> bool:
    try:
        response = supabase.rpc(
            "insert_activity_with_audit",
            {
                "p_user_name": user_name,
                "p_activity_name": activity_name,
                "p_description": description
            }
        ).execute()
        
        print(f"Response from insert_activity_with_audit: {response}")
        return True
    except Exception as e:
        print(f"Exception calling insert_activity_with_audit: {e}")
        return e

