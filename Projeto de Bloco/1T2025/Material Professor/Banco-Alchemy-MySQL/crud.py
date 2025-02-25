from crud_db import *

def consultar_contas():
    contas = consultar_contas_db()
    if (not contas):
        print("Não há contas no banco")
        return
    print("\nContas no banco")
    for conta in contas:
        print(conta)
    print()
