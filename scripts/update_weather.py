"""
Lanza un POST a /actualizar_clima/ y termina.
"""
import os, asyncio, httpx, sys

API   = os.getenv("API_URL")   # p.ej. https://mi-proyecto-production.up.railway.app


if not API:
    sys.exit("API_URL no definido")

async def main():
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{API}/actualizar_clima/"
        )
        r.raise_for_status()
        print(r.json())

if __name__ == "__main__":
    asyncio.run(main())
