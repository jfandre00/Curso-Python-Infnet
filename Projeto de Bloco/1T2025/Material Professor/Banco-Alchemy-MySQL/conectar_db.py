from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conectar_db():
    try:
        engine = create_engine("mysql+pymysql://root:13266199@localhost/banco") #, echo = True)
        #root = usuário, 13266199 = senha, localhost = servidor, banco = nome do banco
        #echo = True, mostra as instruções SQL geradas no console
        Session = sessionmaker(bind=engine)
        session = Session()
        #print("Banco conectado")
    except Exception as ex:
        print("Erro: conexão com o bd")
        exit()
    return session

def desconectar_db(session):
    if (session):
        session.close()

#conectar_db()