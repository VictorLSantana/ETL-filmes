
from dotenv import dotenv_values
import requests

# Importa as variáveis de ambiente do arquivo .env 
env = dotenv_values(dotenv_path='../.env')
api_key = env["api_key"]

# Função que faz a requisição para API de filmes
def conecta_api(titulo, api_key):
    filmes_dict = {}  # dicionário dinâmico
    
    for t in titulo:
        url = f"http://www.omdbapi.com/?t={t}&apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            filmes_dict[t] = data
        
        else:
            raise Exception(f"Erro na requisição: {response.status_code}")
    
    return filmes_dict
    
 
if __name__ == "__main__":
    titulo = ["Inception", "The Godfather", "Esse filme não existe"]

    # Exibe o dicionário
    resultado = conecta_api(titulo, api_key).items()
    for filme, info in resultado:
        print(f"Filme: {filme}")
        print(f"Informações: {info}")
        print()

