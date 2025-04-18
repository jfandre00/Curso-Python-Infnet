import pathlib
from models import Conta

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) + "\\contas.csv"

def ler_contas():
    contas = []
    try:
        with (open(ARQ, "r", encoding="UTF-8") as arquivo):
            while (linha := arquivo.readline()):
                campos = linha.strip("\n").split(",")
                id, nome, saldo = int(campos[0]), campos[1], float(campos[2])
                contas.append(Conta(id, nome, saldo))
    except:
        print("Erro: leitura do arquivo")
    return contas

def gravar_contas(contas):
    try:
        with (open(ARQ, "w", encoding="UTF-8") as arquivo):
            for conta in contas:
                arquivo.write(f"{conta.id},{conta.nome},{conta.saldo}\n")
    except:
        print("Erro: gravação do arquivo")
    