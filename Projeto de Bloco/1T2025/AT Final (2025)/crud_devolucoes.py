from conectar_db import *
import pandas as pd
import datetime # mover para util 


def validar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE id_usuario = ?", (id_usuario,))
    result = cursor.fetchone() is not None
    desconectar(conn)
    return result
    

def verificar_limite_emprestimos(id_usuario):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT COUNT(*) 
        FROM emprestimos 
        WHERE id_usuario = ? AND data_devolucao IS NULL
        ''', (id_usuario,))
        count = cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Erro ao verificar o limite de empréstimos: {e}")
    finally:
        desconectar(conn)
    return count < 5
    

def validar_livro_disponivel(id_livro):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT quantidade_disponivel 
        FROM livros 
        WHERE id_livro = ? AND quantidade_disponivel > 0
        ''', (id_livro,))
        result = cursor.fetchone() is not None
    except sqlite3.Error as e:
        print(f"Erro ao validar livro: {e}")
        result = False
    finally:
        desconectar(conn)
    return result


# Devoluções

### Atenção - estou misturando a logica do negocio com o acesso ao banco
# preciso separar as 2 coisas, pois ai vai funcionar independentemente do banco escolhido.
# regra de negócio do acesso ao banco



def gerenciar_devolucoes():
    conn = conectar()

    print("\n=== REGISTRAR DEVOLUÇÃO ===")
    
    # Listar empréstimos ativos
    print("\nEmpréstimos ativos:")
    query = '''
    SELECT e.id_emprestimo, u.nome || ' ' || u.sobrenome as usuario, 
            l.titulo, e.data_emprestimo
    FROM emprestimos e
    JOIN usuarios u ON e.id_usuario = u.id_usuario
    JOIN livros l ON e.id_livro = l.id_livro
    WHERE e.data_devolucao IS NULL
    ORDER BY e.data_emprestimo
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    
    if df.empty:
        print("Não há empréstimos ativos!")
        return
    
    # Registrar devolução
    while True:
        id_emprestimo = input("\nDigite o ID do empréstimo para devolução (ou 0 para sair): ")
        if id_emprestimo == "0":
            print("Operação de devolução cancelada.")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM emprestimos WHERE id_emprestimo = ? AND data_devolucao IS NULL", (id_emprestimo,))
        if cursor.fetchone():
            break
        else:
            print("ID do empréstimo inválido ou já devolvido. Tente novamente.")
    data_devolucao = datetime.datetime.now().strftime('%Y-%m-%d')
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Obter id_livro para atualizar estoque
        cursor.execute(
            "SELECT id_livro FROM emprestimos WHERE id_emprestimo = ?",
            (id_emprestimo,)
        )
        id_livro = cursor.fetchone()[0]
        
        # Registrar devolução
        cursor.execute(
            "UPDATE emprestimos SET data_devolucao = ? WHERE id_emprestimo = ?",
            (data_devolucao, id_emprestimo)
        )
        
        # Atualizar quantidade disponível
        cursor.execute(
            "UPDATE livros SET quantidade_disponivel = quantidade_disponivel + 1 WHERE id_livro = ?",
            (id_livro,)
        )
        
        conn.commit()
        print("Devolução registrada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao registrar devolução: {e}")
        conn.rollback() # desfaz as alterações em caso de erro
    finally:
        desconectar(conn)

    