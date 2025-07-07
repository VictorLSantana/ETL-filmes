
from sqlalchemy import create_engine
from dotenv import dotenv_values
import pandas as pd



def conectar_bd(user, password, host, database, port):
    """
    Função para conectar ao banco de dados MySQL e enviar um DataFrame.
    """
    # Configurar a conexão com o banco de dados MySQL.
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
    
    print(f"Conectado ao banco de dados {database} com sucesso.")
    
    return engine

def escrever_df_no_bd(engine, df, table_name):
    """
    Função auxiliar para escrever um DataFrame no banco de dados.
    """
    # Enviar o DataFrame para o banco de dados MySQL.
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False) 
    
    print(f"DataFrame escrito na tabela '{table_name}' com sucesso.")



if __name__ == "__main__":
    # Exemplo de uso da função conectar_bd
    env = dotenv_values(dotenv_path='../.env')
    user = env["user"]
    password = env["password"]
    host = env["host"]
    database = env["database"]
    port = env["port"]
    df = pd.DataFrame({'example_column': [1, 2, 3]})  # Exemplo de DataFrame para teste
    conectar_bd(user, password, host, database, port, df, 'nome_da_tabela')
