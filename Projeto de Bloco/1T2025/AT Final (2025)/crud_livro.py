import pandas as pd
from conectar_db import *


def listar_livros():
    conn = conectar()
    print("\n--- CATÁLOGO DE LIVROS ---")
    query = '''
    SELECT l.id_livro, l.titulo, l.genero, l.quantidade_disponivel as disp, 
            GROUP_CONCAT(a.nome, ', ') as autores
    FROM livros l
    LEFT JOIN livro_autor la ON l.id_livro = la.id_livro
    LEFT JOIN autores a ON la.id_autor = a.id_autor
    GROUP BY l.id_livro
    ORDER BY l.titulo
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)

def buscar_livro_titulo():
    conn = conectar()
    termo = input("\nDigite parte do título: ")
    query = '''
    SELECT l.id_livro, l.titulo, l.genero, l.quantidade_disponivel as disp
    FROM livros l
    WHERE l.titulo LIKE ?
    ORDER BY l.titulo
    '''
    df = pd.read_sql_query(query, conn, params=(f'%{termo}%',))
    print(df.to_string(index=False))
    desconectar(conn)

def buscar_livro_autor():
    conn = conectar()
    termo = input("\nDigite o nome do autor: ")
    query = '''
    SELECT l.id_livro, l.titulo, a.nome as autor, l.quantidade_disponivel as disp
    FROM livros l
    JOIN livro_autor la ON l.id_livro = la.id_livro
    JOIN autores a ON la.id_autor = a.id_autor
    WHERE a.nome LIKE ?
    ORDER BY l.titulo
    '''
    df = pd.read_sql_query(query, conn, params=(f'{termo}%',))
    print(df.to_string(index=False))
    desconectar(conn)

def ver_disponibilidade():
    conn = conectar()
    id_livro = input("Digite o ID do livro: ")
    query = '''
    SELECT titulo, quantidade_disponivel as exemplares_disponiveis
    FROM livros
    WHERE id_livro = ?
    '''
    df = pd.read_sql_query(query, conn, params=(id_livro,))
    print(df.to_string(index=False))
    desconectar(conn)