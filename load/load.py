
from sqlalchemy import create_engine
from dotenv import dotenv_values
import pandas as pd


def conectar_bd(user, password, host, database, port):
    """
    Função para conectar ao banco de dados MySQL e enviar um DataFrame.
    """
    # Configurar a conexão com o banco de dados MySQL.
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
    
    return engine

def escrever_df_no_bd(engine, df, table_name):
    """
    Função auxiliar para escrever um DataFrame no banco de dados.
    """
    # Enviar o DataFrame para o banco de dados MySQL.
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False) 
    
    
def interface_usuario_genero(df):
    print("- O banco de dados possui os top 250 filmes do site da IMDB.\n")
    
    # Escolhendo o gênero
    print("- Digite um número para escolher um gênero:\n")
    todos_os_generos = df['Genre'].str.split(', ').explode().unique()
    lista_generos = []
    
    for i, genero in enumerate(todos_os_generos, start=1):
        print(f"{i}. {genero}")
        lista_generos.append(genero)

    print()  # linha em branco
    
    while True:
        entrada = input("Digite o número da opção desejada: ")
        try:
            escolha = int(entrada)
            if 1 <= escolha <= len(lista_generos):
                break
            else:
                print("Opção inválida. Escolha um número dentro da lista.")
        except ValueError:
            print("Entrada inválida. Digite apenas um número.")
    
    genero_escolhido = lista_generos[escolha - 1]
    print(f"\nVocê escolheu o gênero: {genero_escolhido}")
    
    return genero_escolhido

def interface_usuario_diretor(df, genero):
    # Filtra o DataFrame para o gênero escolhido
    df = df[df['Genre'].str.contains(genero, case=False, na=False)]
    
    print("- Agora escolha o diretor do filme que você deseja assistir:\n")
    todos_os_diretores = df['Director'].str.split(', ').explode().unique()
    lista_diretores = []
    
    for i, diretor in enumerate(todos_os_diretores, start=1):
        print(f"{i}. {diretor}")
        lista_diretores.append(diretor)

    print()  # linha em branco
    
    while True:
        entrada = input("Digite o número da opção desejada: ")
        try:
            escolha = int(entrada)
            if 1 <= escolha <= len(lista_diretores):
                break
            else:
                print("Opção inválida. Escolha um número dentro da lista.")
        except ValueError:
            print("Entrada inválida. Digite apenas um número.")
    
    diretor_escolhido = lista_diretores[escolha - 1]
    print(f"\nVocê escolheu o diretor: {diretor_escolhido}")
    
    return diretor_escolhido

def consulta_filme_bd(genero, diretor, engine):
    """
    Consulta o banco de dados e retorna filmes com base no gênero e diretor escolhidos.
    """
    query = """
        SELECT * FROM filmes_imdb
        WHERE Genre LIKE %(genero)s AND Director LIKE %(diretor)s
    """

    # Parâmetros com curingas para LIKE
    params = {
        "genero": f"%{genero}%",
        "diretor": f"%{diretor}%"
    }

    df_filmes = pd.read_sql(query, con=engine, params=params)
    lista_filmes = df_filmes['Title'].tolist()

    if df_filmes.empty:
        print("Nenhum filme encontrado com os critérios selecionados.")
        return None

    print(f"\nFilmes do gênero {genero} dirigidos por {diretor}:\n")
    for i, filme in enumerate(lista_filmes, start=1):
        print(f"{i}. {filme}")
    print()

    # Validação de entrada do usuário
    while True:
        entrada = input("Digite o número da opção desejada: ")
        try:
            escolha = int(entrada)
            if 1 <= escolha <= len(lista_filmes):
                break
            else:
                print("Opção inválida. Escolha um número dentro da lista.")
        except ValueError:
            print("Entrada inválida. Digite apenas um número.")

    filme_escolhido = lista_filmes[escolha - 1]
    print(f"\nÓtima escolha! Você escolheu o filme: {filme_escolhido}\n")

    return filme_escolhido


def caracteristicas_filme(filme, engine):
    """
    Consulta o banco de dados e retorna as características do filme escolhido.
    """
    query = """
        SELECT * FROM filmes_imdb
        WHERE Title LIKE %(filme)s
    """
    params = {
        "filme": f"%{filme}%"  # usando LIKE com curinga
    }

    df_filmes = pd.read_sql(query, con=engine, params=params)

    if df_filmes.empty:
        print("Filme não encontrado.")
        return

    filme_info = df_filmes.iloc[0]  # pega a primeira (e única) linha como Série

    print(f"\nCaracterísticas do filme: {filme_info['Title']}\n")
    print(f"Data de lançamento: {filme_info['Released']}")
    print(f"Duração: {filme_info['Runtime']}")
    print(f"Gênero: {filme_info['Genre']}")
    print(f"Diretor: {filme_info['Director']}")
    print(f"Roteirista: {filme_info['Writer']}")
    print(f"Atores: {filme_info['Actors']}")
    print(f"Sinopse: {filme_info['Plot']}")
    print(f"Idioma: {filme_info['Language']}")
    print(f"País: {filme_info['Country']}")
    print(f"Prêmios: {filme_info['Awards']}")
    print(f"Metascore: {filme_info['Metascore']}")
    print(f"Avaliação IMDb: {filme_info['imdbRating']}")
    print(f"Votos IMDb: {filme_info['imdbVotes']}")
    print(f"Bilheteria: {filme_info['BoxOffice']}")
    
    print("\nEssas são as características do filme que você escolheu. Aproveite o filme!\n")
    
    
    


if __name__ == "__main__":
    # Importa as variáveis de ambiente do arquivo .env 
    env = dotenv_values(dotenv_path='../.env')
    
    user = env["user"]
    password = env["password"]
    host = env["host"]
    database = env["database"]
    port = env["port"]
    engine = conectar_bd(user, password, host, database, port)
    
    df = pd.read_json('../filmes.json', orient='index') # apagar quando for chamar a api
    
    tipo_genero = interface_usuario_genero(df)
    diretor = interface_usuario_diretor(df, tipo_genero)
    filme = consulta_filme_bd(tipo_genero, diretor, engine)
    df_filmes = caracteristicas_filme(filme, engine)
    
