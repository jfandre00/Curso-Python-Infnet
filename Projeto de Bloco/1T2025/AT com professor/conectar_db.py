import sqlite3


DB_NAME = 'biblioteca_tp5_final.db'

def conectar():
    conn = sqlite3.connect(DB_NAME)
    #cursor = conn.cursor()
    #aonde precisar do cursor, precisarei criar novamente, conforme já fiz em alguns casos
    return conn


def desconectar(conn):
    conn.close()