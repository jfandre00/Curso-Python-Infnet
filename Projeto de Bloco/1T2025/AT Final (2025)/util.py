from datetime import datetime

def validador_data_nascimento(data_nascimento):
    try:
        data = datetime.strptime(data_nascimento, "%Y-%m-%d")
        return data
    except ValueError:
        print("Data inválida! O formato correto é AAAA-MM-DD.")
        return None
    
def validador_nome_sobrenome(nome):
    if len(nome) < 3:
        print("Nome deve ter pelo menos 3 caracteres.")
        return False
    return True
