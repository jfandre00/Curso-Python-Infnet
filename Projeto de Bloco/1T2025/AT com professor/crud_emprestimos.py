import datetime # levar ele para o util, só vai ter lá
from conectar_db import *
from crud_devolucoes import *

def gerenciar_emprestimos():
    print("\n=== REALIZAR EMPRÉSTIMO ===")
    
    # Verificar usuário
    id_usuario = input("Digite o ID do usuário: ")
    if not validar_usuario(id_usuario):
        print("Usuário inválido!")
        return
    
    # Verificar limite de empréstimos
    if not verificar_limite_emprestimos(id_usuario):
        print("Usuário atingiu o limite de 5 empréstimos!")
        return
    
    # Verificar livro
    id_livro = input("Digite o ID do livro: ")
    if not validar_livro_disponivel(id_livro):
        print("Livro indisponível ou ID inválido!")
        return
    
    # Registrar empréstimo
    data_emprestimo = datetime.now().strftime('%Y-%m-%d')
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Registrar empréstimo
        cursor.execute(
            "INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (?, ?, ?)",
            (id_usuario, id_livro, data_emprestimo)
        )
        
        # Atualizar quantidade disponível
        cursor.execute(
            "UPDATE livros SET quantidade_disponivel = quantidade_disponivel - 1 WHERE id_livro = ?",
            (id_livro,)
        )
        
        conn.commit()
        print("Empréstimo registrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao registrar empréstimo: {e}")
        #conn.rollback()
    finally:
        desconectar(conn)
        