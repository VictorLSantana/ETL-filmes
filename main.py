
from dotenv import dotenv_values
from extract.get_api import conecta_api
from extract.scraping import raspar_filmes
from transform.formata_titulos import limpar_titulos
# Pipe Line:
# Raspar os títulos de filmes
# Formatar os títulos dos filmes
# Conectar à API para obter informações dos filmes

# Raspando os títulos dos  250 melhores filmes do site IMDB
titulos_texto = raspar_filmes()

# Formatando os títulos dos filmes
titulos_limpos = limpar_titulos(titulos_texto)

# Conectando à API para obter informações dos filmes
# Importa as variáveis de ambiente do arquivo .env 
env = dotenv_values(dotenv_path='.env')
api_key = env["api_key"]

filmes_dict = conecta_api(titulos_limpos, api_key)