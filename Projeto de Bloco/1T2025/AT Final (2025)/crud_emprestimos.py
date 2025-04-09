import datetime 
from conectar_db import *
from crud_devolucoes import *

def gerenciar_emprestimos():
    print("\n=== REALIZAR EMPRÉSTIMO ===")
    
    listar_usuarios_e_livros()

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
    data_emprestimo = datetime.datetime.now().strftime('%Y-%m-%d')
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
        conn.rollback()  # Adicionei rollback para garantir consistência em caso de erro
    finally:
        desconectar(conn)
        
def listar_usuarios_e_livros():

    print("\n=== USUÁRIOS ===")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, nome FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}")
    print("\n=== LIVROS DISPONÍVEIS ===")
    cursor.execute("SELECT id_livro, titulo, quantidade_disponivel FROM livros WHERE quantidade_disponivel > 0")
    livros_disponiveis = cursor.fetchall()
    for livro in livros_disponiveis:
        print(f"ID: {livro[0]}, Título: {livro[1]}, Quantidade: {livro[2]}")
    cursor.close()
    desconectar(conn)
    print("=========================")
