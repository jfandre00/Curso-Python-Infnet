import sqlite3
import os


DB_NAME = 'biblioteca_tp5_final.db'

def conectar():
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    conn = sqlite3.connect(db_path)
    return conn


def desconectar(conn):
    conn.close()