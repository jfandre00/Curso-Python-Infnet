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