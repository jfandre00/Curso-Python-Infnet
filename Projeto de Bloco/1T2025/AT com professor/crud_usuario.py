import sqlite3
import pandas as pd
from conectar_db import *


def cadastrar_usuario():
    print("\n--- CADASTRAR NOVO USUÁRIO ---")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    data_nasc = input("Data de nascimento (AAAA-MM-DD): ") #preciso validar no util !!!!!!!
        
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, sobrenome, data_nascimento) VALUES (?, ?, ?)",
            (nome, sobrenome, data_nasc)
        )
        conn.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        desconectar(conn)
    
def listar_usuarios():
    conn = conectar()
    print("\n--- LISTA DE USUÁRIOS ---")
    df = pd.read_sql_query("SELECT * FROM usuarios ORDER BY nome", conn)
    print(df.to_string(index=False))
    desconectar(conn)

def buscar_usuario():
    conn = conectar()
    termo = input("\nDigite nome ou sobrenome para buscar: ")
    query = '''
    SELECT * FROM usuarios 
    WHERE nome LIKE ? OR sobrenome LIKE ?
    ORDER BY nome
    '''
    df = pd.read_sql_query(query, conn, params=(f'%{termo}%', f'%{termo}%'))
    print(df.to_string(index=False))
    desconectar(conn)