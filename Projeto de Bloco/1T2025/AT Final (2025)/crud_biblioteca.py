import pandas as pd
from conectar_db import *

def relatorio_emprestimos_ativos():
    conn = conectar()
    print("\n--- EMPRÉSTIMOS ATIVOS ---")
    query = '''
    SELECT e.id_emprestimo, u.nome || ' ' || u.sobrenome as usuario, 
            l.titulo, e.data_emprestimo,
            CEIL(julianday('now') - julianday(e.data_emprestimo)) as dias_emprestado
    FROM emprestimos e
    JOIN usuarios u ON e.id_usuario = u.id_usuario
    JOIN livros l ON e.id_livro = l.id_livro
    WHERE e.data_devolucao IS NULL
    ORDER BY e.data_emprestimo
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)

def relatorio_historico_emprestimos():
    conn = conectar()
    print("\n--- HISTÓRICO DE EMPRÉSTIMOS ---")
    query = '''
    SELECT e.id_emprestimo, u.nome || ' ' || u.sobrenome as usuario, 
            l.titulo, e.data_emprestimo, e.data_devolucao,
            CASE 
                WHEN e.data_devolucao IS NULL THEN 'Em aberto'
                ELSE 'Finalizado'
            END as status
    FROM emprestimos e
    JOIN usuarios u ON e.id_usuario = u.id_usuario
    JOIN livros l ON e.id_livro = l.id_livro
    ORDER BY e.data_emprestimo DESC
    LIMIT 50
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)

def relatorio_livros_mais_emprestados():
    conn = conectar()
    print("\n--- LIVROS MAIS EMPRESTADOS ---")
    query = '''
    SELECT l.titulo, COUNT(e.id_emprestimo) as total_emprestimos
    FROM livros l
    LEFT JOIN emprestimos e ON l.id_livro = e.id_livro
    GROUP BY l.id_livro
    ORDER BY total_emprestimos DESC
    LIMIT 10
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)

def relatorio_usuarios_mais_emprestimos():
    conn = conectar()
    print("\n--- USUÁRIOS COM MAIS EMPRÉSTIMOS ---")
    query = '''
    SELECT u.nome || ' ' || u.sobrenome as usuario, 
            COUNT(e.id_emprestimo) as total_emprestimos
    FROM usuarios u
    LEFT JOIN emprestimos e ON u.id_usuario = e.id_usuario
    GROUP BY u.id_usuario
    ORDER BY total_emprestimos DESC
    LIMIT 10
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)

def quantidade_emprestimos_ativos_por_usuario():
    conn = conectar()
    print("\n--- QUANTIDADE DE EMPRÉSTIMOS ATIVOS POR USUÁRIO ---")
    query = '''
    SELECT u.nome || ' ' || u.sobrenome as usuario, 
            COUNT(CASE WHEN e.data_devolucao IS NULL AND e.data_emprestimo IS NOT NULL THEN 1 ELSE NULL END) as emprestimos_ativos
    FROM usuarios u
    LEFT JOIN emprestimos e ON u.id_usuario = e.id_usuario
    GROUP BY u.id_usuario
    ORDER BY emprestimos_ativos DESC
    '''
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    desconectar(conn)
