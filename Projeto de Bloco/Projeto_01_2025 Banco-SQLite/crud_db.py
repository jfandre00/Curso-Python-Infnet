from conectar_db import *
from models import *

def consultar_contas_db():
    comando = "SELECT * FROM contas;"
    contas = []
    try:
        conn = conectar()
        cursor = conn.cursor() #objeto que permite percorrer os registros
        cursor.execute(comando) #rodei o select no banco
        registros = cursor.fetchall() #recupera todos os registros
        for registro in registros:
            conta = Conta(registro[0], registro[1], registro[2]) 
            contas.append(conta) 
    except Exception as ex:
        print(ex)
    finally: #o finally é executado independente do try ou do except
        desconectar(conn)

    return contas

def consultar_conta_db(id):
    comando = "SELECT * FROM contas WHERE id = ?;"
    conta = []
    try:
        conn = conectar()
        cursor = conn.cursor() #objeto que permite percorrer os registros
        cursor.execute(comando, (id,)) #rodei o select no banco
        registro = cursor.fetchall() #recupera o primeiro registro
        if (registro):
            conta = Conta(registro[0][0], registro[0][1], registro[0][2])
    except Exception as ex:
        print(ex)
    finally: #o finally é executado independente do try ou do except
        desconectar(conn)

    return conta
