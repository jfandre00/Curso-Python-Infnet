from crud_db import *

def consultar_contas():
    contas = consultar_contas_db()
    print()
    for conta in contas:
        print(conta)
    print()

