import sqlite3

def criar_banco():
    '''
    Criação do banco de dados e das tabelas necessárias para o projeto

    '''
    # Precisa atualizar o path do banco de dados para o caminho da máquina de cada um
    conn = sqlite3.connect("/c:/Users/jfand/OneDrive/Documents/MeusProjetos/Curso-Python-Infnet/Projeto de Bloco/1T2025/TP4 (2025)/André/biblioteca.db")
    cursor = conn.cursor()

    # Criar tabela de livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id_livro INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            genero TEXT NOT NULL,
            data_publicacao DATE NOT NULL,
            qtd_paginas INTEGER NOT NULL,
            disponibilidade INTEGER NOT NULL
        )
    ''')

    # Criar tabela de autores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id_autor INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            pais_origem TEXT NOT NULL
        )
    ''')

    # Criar tabela de relacionamento livro_autor (N:N)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livro_autor (
            id_livro INTEGER,
            id_autor INTEGER,
            FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
            FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
            PRIMARY KEY (id_livro, id_autor)
        )
    ''')

    # Criar tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            data_nascimento DATE NOT NULL
        )
    ''')

    # Criar tabela de empréstimos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id_livro INTEGER PRIMARY KEY,
            id_usuario INTEGER NOT NULL,
            data_emprestimo DATE NOT NULL,
            data_devolucao DATE,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
            FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")


'''if __name__ == "__main__":
    criar_banco()
    print("Banco de dados criado com sucesso!")'''
