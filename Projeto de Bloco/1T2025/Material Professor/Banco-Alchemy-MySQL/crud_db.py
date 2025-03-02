from conectar_db import *
from models import *

def consultar_contas_db():
    contas = []
    try:
        session = conectar_db()
        contas = session.query(Conta).all()
    except Exception as ex:
        print(ex)
    finally:
        desconectar_db(session)
    return contas

def consultar_conta_db(id):
    try:
        session = conectar_db()
        conta = session.query(Conta).get(id)
    except Exception as ex:
        print(ex)
    finally:
        desconectar_db(session)
    return conta


def incluir_conta_db(conta):
    try:
        session = conectar_db()
        session.add(conta)
        session.commit()
    except Exception as ex:
        print(ex)
    finally: #esse bloco sempre é executado, independente de erro
        desconectar_db(session)

def excluir_conta_db(conta):
    try:
        session = conectar_db()
        session.delete(conta)
        session.commit()
        print("Conta excluída com sucesso")
    except Exception as ex:
        print(ex)
    finally:
        desconectar_db(session)

def alterar_conta_db(conta):
    try:
        session = conectar_db()
        session.query(Conta).filter(Conta.id_cliente == conta.id_cliente).update({"saldo": conta.saldo})
        session.commit()
        print("Conta alterada com sucesso")
    except Exception as ex:
        print(ex)
    finally:
        desconectar_db(session)