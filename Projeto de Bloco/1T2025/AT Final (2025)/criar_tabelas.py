from conectar_db import *

# Criar tabelas usuários e empréstimos se não existirem (as outras vieram do TP5)
# O trabalho de modelagem e criação do banco de dados foi feito durante o TP4.


def criar_tabelas_db():
    conn = conectar()
    cursor = conn.cursor()
    
    # Tabela de usuários (se não existir)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        data_nascimento DATE NOT NULL
    )
    ''')
    
    # Tabela de empréstimos (se não existir)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (
        id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_livro INTEGER NOT NULL,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
        FOREIGN KEY (id_livro) REFERENCES livros (id_livro)
    )
    ''')
    
    conn.commit()
    conn.close()
