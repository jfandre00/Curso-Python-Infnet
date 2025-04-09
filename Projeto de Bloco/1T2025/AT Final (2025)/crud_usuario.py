import sqlite3
import pandas as pd
from conectar_db import *
from util import *


def cadastrar_usuario():
    print("\n--- CADASTRAR NOVO USUÁRIO ---")
    while True:
        nome = input("Nome: ")
        if validador_nome_sobrenome(nome):  # Chama a função de validação
            break
        else:
            print("Nome inválido. Tente novamente.")
    
    while True:
        sobrenome = input("Sobrenome: ")
        if validador_nome_sobrenome(sobrenome):  # Chama a função de validação
            break
        else:
            print("Sobrenome inválido. Tente novamente.")

    # Verificar se o nome e sobrenome já existem no banco de dados antes de cadastrar
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nome = ? AND sobrenome = ?", (nome, sobrenome))
    usuario_existente = cursor.fetchone()[0]  # pega o primeiro elemento da tupla retornada
    if usuario_existente > 0:
        print("Usuário já cadastrado!")
        desconectar(conn)
        return
        

    while True:
        data_nasc = input("Data de nascimento (AAAA-MM-DD): ")
        if validador_data_nascimento(data_nasc): # Chama a função de validação
            break
        else:
            print("Data de nascimento inválida. Tente novamente.")

        
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

def excluir_usuario():
    conn = conectar()
    id_usuario = input("\nDigite o ID do usuário a ser excluído: ")
    
    try:
        cursor = conn.cursor()
        
        # Verifica se o usuário existe
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        usuario = cursor.fetchone()     
        if not usuario:
            print("Usuário não encontrado!")
            return
        
        # Verifica se o usuário possui empréstimos ativos
        cursor.execute("SELECT COUNT(*) FROM emprestimos WHERE id_usuario = ? AND data_devolucao IS NULL", (id_usuario,))
        emprestimos_ativos = cursor.fetchone()[0]  # pega o primeiro elemento da tupla retornada
        
        if emprestimos_ativos > 0:
            print("Não é possível excluir o usuário. Existem empréstimos ativos associados a este usuário.")
            return
        
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        conn.commit()
        print("Usuário excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        desconectar(conn)

def editar_usuario():
    conn = conectar()
    id_usuario = input("\nDigite o ID do usuário a ser editado: ")
    
    # Verifica se o usuário existe
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id_usuario,))
    usuario = cursor.fetchone()
    
    if not usuario:
        print("Usuário não encontrado!")
        return
    
    #Se o usuário não digitar nada, o valor padrão será o que já está no banco de dados
    nome = input(f"Nome ({usuario[1]}): ") or usuario[1]
    sobrenome = input(f"Sobrenome ({usuario[2]}): ") or usuario[2]
    data_nasc = input(f"Data de nascimento ({usuario[3]}): ") or usuario[3]
    
    try:
        cursor.execute(
            "UPDATE usuarios SET nome = ?, sobrenome = ?, data_nascimento = ? WHERE id_usuario = ?",
            (nome, sobrenome, data_nasc, id_usuario)
        )
        conn.commit()
        print("Usuário editado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao editar usuário: {e}")
    finally:
        desconectar(conn)

        