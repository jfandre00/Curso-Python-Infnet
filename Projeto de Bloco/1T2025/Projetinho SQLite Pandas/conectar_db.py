import sqlite3


BANCO = "C:\\Users\\jfand\\OneDrive\\Documents\\MeusProjetos\\Curso-Python-Infnet\\Projeto de Bloco\\1T2025\\Projetinho SQLite Pandas\\turma.db"

# pode usar \\ ou / no caminho do arquivo

def conectar():
    try:
        conn = sqlite3.connect(BANCO)
        print("Conectado ao banco de dados")
    except Exception as ex:
        print(ex)
        return None
    return conn

def desconectar(conn):
    if (conn is not None):
        conn.close()
        print("Banco de dados desconectado")

'''
# testar a conexão
conn = conectar()
desconectar(conn)
'''