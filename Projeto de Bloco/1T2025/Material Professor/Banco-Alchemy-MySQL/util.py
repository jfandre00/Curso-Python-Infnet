#Arquivo utilitário

def entrar_inteiro():
    while (True):
        try:
            num = int(input("Digite o id da conta: "))
            break
        except:
            print("Erro: valor inválido")
    return num
   
