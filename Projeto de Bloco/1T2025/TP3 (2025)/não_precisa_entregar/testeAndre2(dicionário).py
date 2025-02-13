#Nova Agenda, sendo que o nome do contato é a chave de um dicionário para localizar as demais informações. 
#Os telefones de contato e os emails devem ser implementados como listas
#sem utilizar SQLite ou classes.

agenda = {}

def adicionar_contato(nome, endereco, data_nascimento, telefones, emails):
    """Adiciona um contato à agenda."""
    agenda[nome] = {"endereco": endereco, "data_nascimento": data_nascimento, "telefones": telefones, "emails": emails}
    print(f"Contato '{nome}' adicionado com sucesso.")

def listar_contatos():
    """Lista todos os contatos da agenda."""
    for nome, dados in agenda.items():
        print(f"Nome: {nome}")
        print(f"Endereço: {dados['endereco']}")
        print(f"Data de Nascimento: {dados['data_nascimento']}")
        print(f"Telefones: {', '.join(dados['telefones'])}")
        print(f"Emails: {', '.join(dados['emails'])}")
        print()

def excluir_contato(nome):
    """Exclui um contato da agenda."""
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' excluído com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def alterar_contato(nome, endereco, data_nascimento, telefones, emails):
    """Altera um contato na agenda."""
    if endereco:
        agenda[nome]["endereco"] = endereco
    if data_nascimento:
        agenda[nome]["data_nascimento"] = data_nascimento
    if telefones:
        agenda[nome]["telefones"] = telefones
    if emails:
        agenda[nome]["emails"] = emails
    print(f"Contato '{nome}' alterado com sucesso.")

def menu():
    while True:
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Excluir Contato")
        print("4 - Alterar Contato")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome do contato: ")
            endereco = input("Endereço Completo: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            telefones = input("Telefones (separados por vírgula): ").split(",")
            emails = input("Emails (separados por vírgula): ").split(",")
            adicionar_contato(nome, endereco, data_nascimento, telefones, emails)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            nome = input("Nome do contato a excluir: ")
            excluir_contato(nome)
        elif opcao == "4":
            nome = input("Nome do contato a alterar: ")
            endereco = input("Endereço: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            telefones = input("Telefones (separados por vírgula): ").split(",")
            emails = input("Emails (separados por vírgula): ").split(",")
            alterar_contato(nome, endereco, data_nascimento, telefones, emails)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
        

if __name__ == "__main__":
    menu()


