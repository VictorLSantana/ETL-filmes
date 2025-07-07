
from extract.extract import conecta_api, raspar_filmes
from transform.transform import limpar_titulos
from load.load import conectar_bd, escrever_df_no_bd

from dotenv import dotenv_values
import pandas as pd

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



# Raspando os títulos dos  250 melhores filmes do site IMDB
titulos_texto = raspar_filmes()

# Formatando os títulos dos filmes
titulos_limpos = limpar_titulos(titulos_texto)

# Conectando à API para obter informações dos filmes
api_key = env["api_key"]
filmes_dict = conecta_api(titulos_limpos, api_key)


# Criando um DataFrame com as informações dos filmes
# Selecionando as características que serão exibidas
caracteristicas = [
    "Title",
    "Year",
    "Rated",
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

# Filtra apenas as colunas desejadas
df = df[caracteristicas]

# Tratando valores ausentes
df = df.replace("N/A", pd.NA)

# Formatando a coluna Runtime para inteiro
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(pd.Int64Dtype())

# Formatando a coluna Year para inteiro
df["Year"] = df["Year"].astype(pd.Int64Dtype())

# Formatando a coluna Metascore para inteiro
df["Metascore"] = df["Metascore"].astype(pd.Int64Dtype())

# Formatando a coluna imdbVotes para inteiro
df["imdbVotes"] = df["imdbVotes"].str.replace(",", "").astype(pd.Int64Dtype())

# Formatando a coluna BoxOffice para inteiro
df["BoxOffice"] = df["BoxOffice"].str.replace("$", "").str.replace(",", "").astype(pd.Int64Dtype())

# Formatando a coluna imdbRating para float
df["imdbRating"] = df["imdbRating"].astype(float)

# Conectando ao banco de dados MySQL
user = env["user"]
password = env["password"]
host = env["host"]
database = env["database"]
port = env["port"]
engine = conectar_bd(user, password, host, database, port)

# Enviando o DataFrame para o banco de dados MySQL
escrever_df_no_bd(engine, df, 'filmes_imdb')

#######################
todos_os_generos = df['Genre'].str.split(', ').explode().unique()
contagem_generos = df['Genre'].str.split(', ').explode().value_counts()
print("Todos os gêneros disponíveis: ", todos_os_generos)

df[df['Genre'].str.contains("Music")]
#######################