import sqlite3
import pandas as pd

def ler_dados():
    '''
    Criação e inserção dos DataFrames a partir dos arquivos CSV fornecidos pelo professor
    
    '''

    # Conectar ao banco de dados (ou criar se não existir)
    # Cuidado novamente com o path do banco de dados
    conn = sqlite3.connect("/c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/biblioteca.db")
    cursor = conn.cursor()

    # Lendo os arquivos CSV fornecidos pelo professor e armazenando em DataFrames separados
    df_livros = pd.read_csv('c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/dados/livros.csv')
    df_autores = pd.read_csv('c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/dados/autores.csv')
    df_usuarios = pd.read_csv('c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/dados/usuarios.csv')
    df_emprestimos = pd.read_csv('c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/dados/emprestimos.csv')
    df_livro_autor = pd.read_csv('c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/dados/livros_autores.csv')  

    # Inserindo os dados dos arquivos CSV nas tabelas do banco de dados
    df_livros.to_sql('livros', conn, if_exists='append', index=False)
    df_autores.to_sql('autores', conn, if_exists='append', index=False)
    df_usuarios.to_sql('usuarios', conn, if_exists='append', index=False)
    df_emprestimos.to_sql('emprestimos', conn, if_exists='append', index=False)
    df_livro_autor.to_sql('livro_autor', conn, if_exists='append', index=False)


    conn.commit()
    conn.close()
    print("Leitura dos dados, criação e inserção dos DataFrames finalizada com sucesso!")



