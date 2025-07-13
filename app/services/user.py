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