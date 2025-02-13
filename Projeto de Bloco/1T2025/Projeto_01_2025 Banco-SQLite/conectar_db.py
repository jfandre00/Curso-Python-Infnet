import sqlite3
import os.path

#criando uma constante para o nome do banco
BANCO = "banco.db" 

#criando uma constante para o diretorio do banco
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

#concatenando o diretorio com o nome do banco
DIR_BANCO = os.path.join(BASE_DIR, BANCO)

#print(DIR_BANCO) #imprime o diretorio do banco, somente para teste


#Verificar se o banco existe
def verificar_db():
    if (not os.path.exists(DIR_BANCO)):
        print("Banco de dados não existe")
        exit()

def conectar():
    conn = None
    try:
        conn = sqlite3.connect(DIR_BANCO)
        #print("Banco Conectado!")
    except Exception as ex:
        print(ex)
    return conn

def desconectar(conn):
    if (conn is not None):
        conn.close()
        #print("Banco Desconectado!")




