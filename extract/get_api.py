
from dotenv import dotenv_values
import requests

# Load environment variables from .env file
env = dotenv_values(dotenv_path='.env')
api_key = env["api_key"]


titulo = "Inception"
url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for k, v in data.items():
        print(f"{k}: {v}")
else:
    print("Erro na requisição:", response.status_code)
