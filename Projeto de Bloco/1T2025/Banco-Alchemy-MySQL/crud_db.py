from conectar_db import *
from models import *

def consultar_contas_db():
    contas = []
    try:
        conn = conectar_db()
        #contas = conn.query(Conta).all() -> linhas 9 a 16 foram para substituir essa linha
        print("Consulta realizada com sucesso")
        cursor = conn.cursor()
        cursor.execute("select * from cliente")

        rows = cursor.fetchall()
        for row in rows:
            row = Conta(row[0], row[1], row[2])
            contas.append(row)
    except Exception as ex:
        print(ex)
    finally: #o finally é executado independente do try ou do except
        desconectar_db(conn)
    return contas


