import sqlite3
import pandas as pd

def consultar_banco():
    """
    Realiza três consultas diferentes em um banco de dados SQLite, imprime na tela os resultados e os salva em arquivos JSON.

    Parâmetros: None
    Retorno: None
    Observação: O parâmetro `indent=4` utilizado na função `to_json` define a indentação do arquivo JSON gerado, facilitando a leitura do arquivo.
    """
    conn = sqlite3.connect("/c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/biblioteca.db")

    # Primeira consulta - Autores do livro "Piquenique na Estrada"
    query1 = '''
        SELECT autores.nome
        FROM autores
        JOIN livro_autor ON autores.id_autor = livro_autor.id_autor
        JOIN livros ON livro_autor.id_livro = livros.id_livro
        WHERE livros.titulo = "Piquenique na Estrada"
    '''
    df1 = pd.read_sql_query(query1, conn)
    print("\nAutores do livro 'Piquenique na Estrada':")
    print(df1)

    # Segunda consulta - Livros do autor "Philip K. Dick"
    query2 = '''
        SELECT livros.titulo
        FROM livros
        JOIN livro_autor ON livros.id_livro = livro_autor.id_livro
        JOIN autores ON livro_autor.id_autor = autores.id_autor
        WHERE autores.nome = "Philip K. Dick"
    '''
    df2 = pd.read_sql_query(query2, conn)
    print("\nLivros do Autor 'Philip K. Dick'")
    print(df2)

    # Terceira consulta - Empréstimos atuais do usuário "Pedro Vinicius"
    query3 = '''
        SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao
        FROM emprestimos
        JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
        JOIN livros ON emprestimos.id_livro = livros.id_livro
        WHERE usuarios.nome = "Pedro" AND usuarios.sobrenome = "Vinicius" AND emprestimos.data_devolucao IS NULL
    '''
    df3 = pd.read_sql_query(query3, conn)
    print("\nEmpréstimos atuais do usuário 'Pedro Vinicius'")
    print(df3)

    # Salvando os data frames em arquivos JSON
    df1.to_json("c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/consulta01.json", orient="records", indent=4)
    df2.to_json("c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/consulta02.json", orient="records", indent=4)
    df3.to_json("c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/consulta03.json", orient="records", indent=4)

    conn.close()
    print("\nConsultas realizadas com sucesso!")
    print("Resultados salvos em arquivos JSON.")

#consultar_banco()


