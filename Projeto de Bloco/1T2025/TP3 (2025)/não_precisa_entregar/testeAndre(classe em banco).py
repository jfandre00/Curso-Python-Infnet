class Agenda:
    """Classe para gerenciar uma agenda de contatos."""

    def __init__(self):
        """Inicializa a agenda como um dicionário vazio."""
        self.agenda = {}

    def adicionar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        """Adiciona ou atualiza um contato na agenda."""
        self.agenda[nome] = {
            "endereco": endereco,
            "data_nascimento": data_nascimento,
            "telefones": telefones,
            "emails": emails,
        }
        print(f"Contato '{nome}' salvo com sucesso.")

    def listar_contatos(self):
        """Lista todos os contatos da agenda."""
        if not self.agenda:
            print("A agenda está vazia.")
            return

        for nome, dados in self.agenda.items():
            print(f"\nNome: {nome}")
            print(f"Endereço: {dados['endereco']}")
            print(f"Data de Nascimento: {dados['data_nascimento']}")
            print(f"Telefones: {', '.join(dados['telefones'])}")
            print(f"Emails: {', '.join(dados['emails'])}")
        print()

    def excluir_contato(self, nome):
        """Exclui um contato da agenda."""
        if self.agenda.pop(nome, None) is not None:
            print(f"Contato '{nome}' excluído com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def alterar_contato(self, nome, endereco=None, data_nascimento=None, telefones=None, emails=None):
        """Altera um contato na agenda."""
        if nome not in self.agenda:
            print(f"Contato '{nome}' não encontrado.")
            return
        
        contato = self.agenda[nome]
        if endereco:
            contato["endereco"] = endereco
        if data_nascimento:
            contato["data_nascimento"] = data_nascimento
        if telefones:
            contato["telefones"] = telefones
        if emails:
            contato["emails"] = emails
        
        print(f"Contato '{nome}' alterado com sucesso.")

    def mostrar_dados(self):
        """Mostra todos os dados armazenados na agenda."""
        print(self.agenda)


def menu():
    """Interface de interação com o usuário."""
    agenda = Agenda()

    while True:
        print("\nMENU")
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Excluir Contato")
        print("4 - Alterar Contato")
        print("5 - Mostrar dados internos")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do contato: ").strip()
            endereco = input("Endereço Completo: ").strip()
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()
            telefones = [t.strip() for t in input("Telefones (separados por vírgula): ").split(",")]
            emails = [e.strip() for e in input("Emails (separados por vírgula): ").split(",")]
            agenda.adicionar_contato(nome, endereco, data_nascimento, telefones, emails)

        elif opcao == "2":
            agenda.listar_contatos()

        elif opcao == "3":
            nome = input("Nome do contato a excluir: ").strip()
            agenda.excluir_contato(nome)

        elif opcao == "4":
            nome = input("Nome do contato a alterar: ").strip()
            if nome not in agenda.agenda:
                print(f"Contato '{nome}' não encontrado.")
                continue

            print("\nOpções de alteração:")
            print("1 - Endereço")
            print("2 - Data de Nascimento")
            print("3 - Telefones")
            print("4 - Emails")
            escolha = input("Escolha o que deseja alterar: ")

            if escolha == "1":
                endereco = input("Novo endereço: ").strip()
                agenda.alterar_contato(nome, endereco=endereco)
            elif escolha == "2":
                data_nascimento = input("Nova data de nascimento (DD/MM/AAAA): ").strip()
                agenda.alterar_contato(nome, data_nascimento=data_nascimento)
            elif escolha == "3":
                telefones = [t.strip() for t in input("Novos telefones (separados por vírgula): ").split(",")]
                agenda.alterar_contato(nome, telefones=telefones)
            elif escolha == "4":
                emails = [e.strip() for e in input("Novos emails (separados por vírgula): ").split(",")]
                agenda.alterar_contato(nome, emails=emails)
            else:
                print("Opção inválida.")

        elif opcao == "5":
            agenda.mostrar_dados()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

