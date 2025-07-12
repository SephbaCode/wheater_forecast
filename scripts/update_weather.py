# update_weather.py
import os
import requests

def main() -> None:
    url   = os.environ["UPDATE_URL"]          # ej: https://wheater-forecast.up.railway.app/actualizar
    token = os.environ.get("API_TOKEN", "")   # si tu endpoint usa auth

    resp = requests.post(url, headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    print("Clima actualizado:", resp.status_code)

if __name__ == "__main__":
    main()