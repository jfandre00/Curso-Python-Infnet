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


def incluir_conta_db(nome, saldo):
    comando = "INSERT INTO contas (nome, saldo) VALUES (?, ?);"
    try:
        conn = conectar()
        cursar = conn.cursor()
        cursar.execute(comando, (nome, saldo)) #é uma tupla que é passada como parametro
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def excluir_conta_db(id):
    comando = "DELETE FROM contas WHERE id = ?;"
    try:
        conn = conectar()
        cursar = conn.cursor()
        cursar.execute(comando, (id,)) #é uma tupla que é passada como parametro
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def alterar_conta_db(conta):
    comando = "UPDATE contas SET saldo = ? WHERE id = ?;"
    try:
        conn = conectar()
        cursar = conn.cursor()
        cursar.execute(comando, (conta.saldo, conta.id)) #é uma tupla que é passada como parametro
        #estamos passando dentro da tupla os elementos que estão dentro do objeto conta, que passamos por parametro
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
