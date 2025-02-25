from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conectar_db():
    try:
        engine = create_engine("mysql+pymysql://root:jfandre@localhost/banco") #, echo = True)
        Session = sessionmaker(bind=engine)
        session = Session()
        print("Banco conectado")
    except Exception as ex:
        print("Erro: conexão com o bd")
        exit()
    return session

def desconectar_db(session):
    if (session):
        session.close()

#conectar_db()