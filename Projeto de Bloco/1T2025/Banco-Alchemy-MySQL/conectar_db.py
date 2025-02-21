#import mysql.connector - não funcionou no meu caso, precisei usar o pymysql
import pymysql

def conectar_db():
    conn = None
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="13266199",
            database="banco"
        )
        print("Conexão com o banco de dados realizada com sucesso")
        return conn
    except Exception as ex:
        print(ex)
        print("Erro: conexão com o banco de dados")
        exit()

def desconectar_db(conn):
    if conn:
        conn.close()
        print("Desconexão com o banco de dados realizada com sucesso")

'''
# Testar a conexão e trazer as contas
con = conectar_db()
cursor = con.cursor()
cursor.execute("select * from cliente")

rows = cursor.fetchall()
for row in rows:
    print(row)

desconectar_db(con)
'''