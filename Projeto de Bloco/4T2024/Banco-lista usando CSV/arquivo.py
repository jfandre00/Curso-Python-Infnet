import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) +  '\\contas.csv'
# \\ serve para escapar o caractere \, pois ele é reservado

def ler_contas():
    contas = []
    try:
        with (open(ARQ, "r", encoding="UTF-8") as arquivo):
            while (linha := arquivo.readline()):
                campos = linha.strip("\n").split(",")
                id, nome, saldo = int(campos[0]), campos[1], float(campos[2])
                contas.append([id, nome, saldo])
    except:
        print("Erro ao ler o arquivo")
    return contas


def gravar_contas(contas):
    # gravar contas no arquivo
    try:
        with (open(ARQ, "w", encoding="UTF-8") as arquivo):
            for conta in contas:
                arquivo.write(f"{conta[0]},{conta[1]},{conta[2]}\n")
    except:
        print("Erro ao gravar o arquivo")



