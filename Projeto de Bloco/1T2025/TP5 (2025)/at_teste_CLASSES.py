import sqlite3
from datetime import datetime
import pandas as pd

class Biblioteca:
    def __init__(self, db_name='biblioteca_tp5_final.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def __del__(self):
        self.conn.close()
    
    def mostrar_menu_principal(self):
        while True:
            print("\n=== SISTEMA DE BIBLIOTECA ===")
            print("1. Gerenciar Usuários")
            print("2. Gerenciar Livros")
            print("3. Empréstimos")
            print("4. Devoluções")
            print("5. Relatórios")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.mostrar_menu_usuarios()
            elif opcao == '2':
                self.mostrar_menu_livros()
            elif opcao == '3':
                self.gerenciar_emprestimos()
            elif opcao == '4':
                self.gerenciar_devolucoes()
            elif opcao == '5':
                self.mostrar_menu_relatorios()
            elif opcao == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
    
    # Menu de Usuários
    def mostrar_menu_usuarios(self):
        while True:
            print("\n=== GERENCIAR USUÁRIOS ===")
            print("1. Cadastrar novo usuário")
            print("2. Listar todos os usuários")
            print("3. Buscar usuário")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.cadastrar_usuario()
            elif opcao == '2':
                self.listar_usuarios()
            elif opcao == '3':
                self.buscar_usuario()
            elif opcao == '0':
                break
            else:
                print("Opção inválida!")
    
    def cadastrar_usuario(self):
        print("\n--- CADASTRAR NOVO USUÁRIO ---")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        data_nasc = input("Data de nascimento (AAAA-MM-DD): ")
        
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (nome, sobrenome, data_nascimento) VALUES (?, ?, ?)",
                (nome, sobrenome, data_nasc)
            )
            self.conn.commit()
            print("Usuário cadastrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
    
    def listar_usuarios(self):
        print("\n--- LISTA DE USUÁRIOS ---")
        df = pd.read_sql_query("SELECT * FROM usuarios ORDER BY nome", self.conn)
        print(df.to_string(index=False))
    
    def buscar_usuario(self):
        termo = input("\nDigite nome ou sobrenome para buscar: ")
        query = '''
        SELECT * FROM usuarios 
        WHERE nome LIKE ? OR sobrenome LIKE ?
        ORDER BY nome
        '''
        df = pd.read_sql_query(query, self.conn, params=(f'%{termo}%', f'%{termo}%'))
        print(df.to_string(index=False))
    
    # Menu de Livros
    def mostrar_menu_livros(self):
        while True:
            print("\n=== GERENCIAR LIVROS ===")
            print("1. Listar todos os livros")
            print("2. Buscar livro por título")
            print("3. Buscar livro por autor")
            print("4. Ver disponibilidade")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.listar_livros()
            elif opcao == '2':
                self.buscar_livro_titulo()
            elif opcao == '3':
                self.buscar_livro_autor()
            elif opcao == '4':
                self.ver_disponibilidade()
            elif opcao == '0':
                break
            else:
                print("Opção inválida!")
    
    def listar_livros(self):
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
        df = pd.read_sql_query(query, self.conn)
        print(df.to_string(index=False))
    
    def buscar_livro_titulo(self):
        termo = input("\nDigite parte do título: ")
        query = '''
        SELECT l.id_livro, l.titulo, l.genero, l.quantidade_disponivel as disp
        FROM livros l
        WHERE l.titulo LIKE ?
        ORDER BY l.titulo
        '''
        df = pd.read_sql_query(query, self.conn, params=(f'%{termo}%',))
        print(df.to_string(index=False))
    
    def buscar_livro_autor(self):
        termo = input("\nDigite parte do nome do autor: ")
        query = '''
        SELECT l.id_livro, l.titulo, a.nome as autor, l.quantidade_disponivel as disp
        FROM livros l
        JOIN livro_autor la ON l.id_livro = la.id_livro
        JOIN autores a ON la.id_autor = a.id_autor
        WHERE a.nome LIKE ?
        ORDER BY l.titulo
        '''
        df = pd.read_sql_query(query, self.conn, params=(f'%{termo}%',))
        print(df.to_string(index=False))
    
    def ver_disponibilidade(self):
        id_livro = input("Digite o ID do livro: ")
        query = '''
        SELECT titulo, quantidade_disponivel as exemplares_disponiveis
        FROM livros
        WHERE id_livro = ?
        '''
        df = pd.read_sql_query(query, self.conn, params=(id_livro,))
        print(df.to_string(index=False))
    
    # Empréstimos
    def gerenciar_emprestimos(self):
        print("\n=== REALIZAR EMPRÉSTIMO ===")
        
        # Verificar usuário
        id_usuario = input("Digite o ID do usuário: ")
        if not self.validar_usuario(id_usuario):
            print("Usuário inválido!")
            return
        
        # Verificar limite de empréstimos
        if not self.verificar_limite_emprestimos(id_usuario):
            print("Usuário atingiu o limite de 5 empréstimos!")
            return
        
        # Verificar livro
        id_livro = input("Digite o ID do livro: ")
        if not self.validar_livro_disponivel(id_livro):
            print("Livro indisponível ou ID inválido!")
            return
        
        # Registrar empréstimo
        data_emprestimo = datetime.now().strftime('%Y-%m-%d')
        try:
            # Registrar empréstimo
            self.cursor.execute(
                "INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (?, ?, ?)",
                (id_usuario, id_livro, data_emprestimo)
            )
            
            # Atualizar quantidade disponível
            self.cursor.execute(
                "UPDATE livros SET quantidade_disponivel = quantidade_disponivel - 1 WHERE id_livro = ?",
                (id_livro,)
            )
            
            self.conn.commit()
            print("Empréstimo registrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao registrar empréstimo: {e}")
            self.conn.rollback()
    
    def validar_usuario(self, id_usuario):
        self.cursor.execute("SELECT 1 FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        return self.cursor.fetchone() is not None
    
    def verificar_limite_emprestimos(self, id_usuario):
        self.cursor.execute('''
        SELECT COUNT(*) 
        FROM emprestimos 
        WHERE id_usuario = ? AND data_devolucao IS NULL
        ''', (id_usuario,))
        count = self.cursor.fetchone()[0]
        return count < 5
    
    def validar_livro_disponivel(self, id_livro):
        self.cursor.execute('''
        SELECT quantidade_disponivel 
        FROM livros 
        WHERE id_livro = ? AND quantidade_disponivel > 0
        ''', (id_livro,))
        return self.cursor.fetchone() is not None
    
    # Devoluções
    def gerenciar_devolucoes(self):
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
        df = pd.read_sql_query(query, self.conn)
        print(df.to_string(index=False))
        
        if df.empty:
            print("Não há empréstimos ativos!")
            return
        
        # Registrar devolução
        id_emprestimo = input("\nDigite o ID do empréstimo para devolução: ")
        data_devolucao = datetime.now().strftime('%Y-%m-%d')
        
        try:
            # Obter id_livro para atualizar estoque
            self.cursor.execute(
                "SELECT id_livro FROM emprestimos WHERE id_emprestimo = ?",
                (id_emprestimo,)
            )
            id_livro = self.cursor.fetchone()[0]
            
            # Registrar devolução
            self.cursor.execute(
                "UPDATE emprestimos SET data_devolucao = ? WHERE id_emprestimo = ?",
                (data_devolucao, id_emprestimo)
            )
            
            # Atualizar quantidade disponível
            self.cursor.execute(
                "UPDATE livros SET quantidade_disponivel = quantidade_disponivel + 1 WHERE id_livro = ?",
                (id_livro,)
            )
            
            self.conn.commit()
            print("Devolução registrada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao registrar devolução: {e}")
            self.conn.rollback()
    
    # Relatórios
    def mostrar_menu_relatorios(self):
        while True:
            print("\n=== RELATÓRIOS ===")
            print("1. Empréstimos ativos")
            print("2. Histórico de empréstimos")
            print("3. Livros mais emprestados")
            print("4. Usuários com mais empréstimos")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.relatorio_emprestimos_ativos()
            elif opcao == '2':
                self.relatorio_historico_emprestimos()
            elif opcao == '3':
                self.relatorio_livros_mais_emprestados()
            elif opcao == '4':
                self.relatorio_usuarios_mais_emprestimos()
            elif opcao == '0':
                break
            else:
                print("Opção inválida!")
    
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


# Criar tabelas se não existirem (incluindo a tabela de empréstimos)
def criar_tabelas():
    conn = sqlite3.connect('biblioteca_tp5.db')
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

# Inicializar o sistema
if __name__ == "__main__":
    print("=== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ===")
    print("Inicializando banco de dados...")
    criar_tabelas()
    
    biblioteca = Biblioteca()
    biblioteca.mostrar_menu_principal()