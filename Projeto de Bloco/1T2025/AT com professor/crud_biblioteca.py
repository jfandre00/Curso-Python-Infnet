import pandas as pd


def relatorio_emprestimos_ativos(self):
    print("\n--- EMPRÉSTIMOS ATIVOS ---")
    query = '''
    SELECT e.id_emprestimo, u.nome || ' ' || u.sobrenome as usuario, 
            l.titulo, e.data_emprestimo,
            julianday('now') - julianday(e.data_emprestimo) as dias_emprestado
    FROM emprestimos e
    JOIN usuarios u ON e.id_usuario = u.id_usuario
    JOIN livros l ON e.id_livro = l.id_livro
    WHERE e.data_devolucao IS NULL
    ORDER BY e.data_emprestimo
    '''
    df = pd.read_sql_query(query, self.conn)
    print(df.to_string(index=False))

def relatorio_historico_emprestimos(self):
    print("\n--- HISTÓRICO DE EMPRÉSTIMOS ---")
    query = '''
    SELECT e.id_emprestimo, u.nome || ' ' || u.sobrenome as usuario, 
            l.titulo, e.data_emprestimo, e.data_devolucao,
            CASE 
                WHEN e.data_devolucao IS NULL THEN 'Em aberto'
                ELSE e.data_devolucao
            END as status
    FROM emprestimos e
    JOIN usuarios u ON e.id_usuario = u.id_usuario
    JOIN livros l ON e.id_livro = l.id_livro
    ORDER BY e.data_emprestimo DESC
    LIMIT 50
    '''
    df = pd.read_sql_query(query, self.conn)
    print(df.to_string(index=False))

def relatorio_livros_mais_emprestados(self):
    print("\n--- LIVROS MAIS EMPRESTADOS ---")
    query = '''
    SELECT l.titulo, COUNT(e.id_emprestimo) as total_emprestimos
    FROM livros l
    LEFT JOIN emprestimos e ON l.id_livro = e.id_livro
    GROUP BY l.id_livro
    ORDER BY total_emprestimos DESC
    LIMIT 10
    '''
    df = pd.read_sql_query(query, self.conn)
    print(df.to_string(index=False))

def relatorio_usuarios_mais_emprestimos(self):
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
    df = pd.read_sql_query(query, self.conn)
    print(df.to_string(index=False))
