
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
    print(f"{'='*20} INTERFACE DE RECOMENDAÇÃO DE FILMES {'='*20}\n")
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

    


if __name__ == "__main__":
    df = pd.read_json('../filmes.json', orient='index') # apagar quando for chamar a api
    genero = interface_usuario(df, 'Genre')
    print(genero)

