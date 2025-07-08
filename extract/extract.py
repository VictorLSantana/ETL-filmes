
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


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

# Função para retornar nome dos 250 melhores filmes do IMDB
def raspar_filmes():
    # === Configurações iniciais ===
    url_pagina = "https://www.imdb.com/chart/top"

    # Setup do Chrome
    options = Options()
    options.add_argument("--lang=en-US")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url_pagina)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)  # Tempo máximo de espera por elemento

    # === Raspando nome dos filmes ===
    
    
    # Aguarda até os elementos estarem carregados
    wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, 'h3.ipc-title__text.ipc-title__text--reduced')
    ))

    # Coleta os textos dos <h3>
    titulos = driver.find_elements(By.CSS_SELECTOR, 'h3.ipc-title__text.ipc-title__text--reduced')
    titulos_texto = [titulo.text for titulo in titulos]
    
    #Fecha o navegador após o pedido
    driver.quit()
    
    return titulos_texto
    
 
if __name__ == "__main__":
    
    # === Executa a função de conectar á API ===
    env = dotenv_values(dotenv_path='../.env')
    api_key = env["api_key"]
    titulo = ["Inception", "The Godfather", "Esse filme não existe"]
    resultado = conecta_api(titulo, api_key).items()
    for filme, info in resultado:
        print(f"Filme: {filme}")
        print(f"Informações: {info}")
        print()
    
    # === Executa a função de raspagem de filmes ===
    filmes = raspar_filmes()
    for filme in filmes:
        print(filme)
        print()