

from extract.extract import conecta_api, raspar_filmes
from transform.transform import limpar_titulos
from load.load import conectar_bd, escrever_df_no_bd, interface_usuario_genero, interface_usuario_diretor, consulta_filme_bd, caracteristicas_filme

from dotenv import dotenv_values
import pandas as pd
import warnings
import time
warnings.filterwarnings("ignore")

# Importa as variáveis de ambiente do arquivo .env 
env = dotenv_values(dotenv_path='.env')

# ==== Pipe Line ====: (Extract, Transform, Load)

# ==== EXTRACT ====:
# Raspar os títulos de filmes
# Conectar à API para obter informações dos filmes


# ==== TRANSFORM ====:
# Formatar os títulos dos filmes
# Tratamento dos dados


# ==== LOAD ====:
# Conectar ao banco de dados
# Enviar o dataframe para o banco de dados MySQL
# Interface de usuário para recomendação de filmes



# Raspando os títulos dos  250 melhores filmes do site IMDB
print(f"{'='*20} INTERFACE DE RECOMENDAÇÃO DE FILMES {'='*20}\n")
print("- Entrando no site 'https://www.imdb.com/chart/top' para baixar as informações dos filmes...\n")
time.sleep(5)  # Pausa de 5 segundos para simular o tempo de carregamento da página
titulos_texto = raspar_filmes()

# Formatando os títulos dos filmes17
titulos_limpos = limpar_titulos(titulos_texto)

# Conectando à API para obter informações dos filmes
api_key = env["api_key"]
filmes_dict = conecta_api(titulos_limpos, api_key)
#filmes_dict = pd.read_json('filmes.json', orient='index') # apagar quando for chamar a api



# Criando um DataFrame com as informações dos filmes
# Selecionando as características que serão exibidas
caracteristicas = [
    "Title",
    "Released",
    "Runtime",
    "Genre",
    "Director",
    "Writer",
    "Actors",
    "Plot",
    "Language",
    "Country",
    "Awards",
    "Metascore",
    "imdbRating",
    "imdbVotes",
    "BoxOffice"
]

# Cria DataFrame com todas as colunas, uma linha por filme
df = pd.DataFrame.from_dict(filmes_dict, orient="index")
#df = filmes_dict # apagar quando for chamar a api

# Filtra apenas as colunas desejadas
df = df[caracteristicas]


 # Substitui valores "N/A" por "pd.NA"
df = df.replace("N/A", pd.NA) 

# Formatando a coluna Runtime para inteiro
def converter_minutos_para_horas(minutos):
    horas, resto = divmod(minutos, 60)
    return f"{horas}h {resto}min"

df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(pd.Int64Dtype())
df["Runtime"] = df["Runtime"].apply(converter_minutos_para_horas)


# Conectando ao banco de dados MySQL
user = env["user"]
password = env["password"]
host = env["host"]
database = env["database"]
port = env["port"]
engine = conectar_bd(user, password, host, database, port)

# Enviando o DataFrame para o banco de dados MySQL
escrever_df_no_bd(engine, df, 'filmes_imdb')

# Interface de usuário para recomendação de filmes
genero = interface_usuario_genero(df)
diretor = interface_usuario_diretor(df, genero)
filme = consulta_filme_bd(genero, diretor, engine)
caracteristicas_filme(filme, engine)

