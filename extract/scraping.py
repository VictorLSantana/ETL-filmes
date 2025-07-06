
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Função para retornar nome dos 250 melhores filmes do IMDB
def get_movies():
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
    # Executa a função e imprime os resultados
    filmes = get_movies()
    for filme in filmes:
        print(filme)
        print("\n")