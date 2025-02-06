import sqlite3
import os

class Agenda:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "agenda.db"))
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                nome TEXT PRIMARY KEY,
                endereco TEXT,
                data_nascimento TEXT,
                telefones TEXT,
                emails TEXT
            )
        ''')
        self.conn.commit()

    def adicionar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        """Adiciona ou atualiza um contato na agenda."""
        telefones_str = ",".join(telefones)
        emails_str = ",".join(emails)
        self.cursor.execute("""
            INSERT INTO contatos (nome, endereco, data_nascimento, telefones, emails) 
            VALUES (?, ?, ?, ?, ?) 
            ON CONFLICT(nome) DO UPDATE SET endereco=excluded.endereco, data_nascimento=excluded.data_nascimento, telefones=excluded.telefones, emails=excluded.emails
        """, (nome, endereco, data_nascimento, telefones_str, emails_str))
        self.conn.commit()
        print(f"Contato '{nome}' adicionado/atualizado com sucesso.")

    def remover_contato(self, nome):
        """Remove um contato da agenda."""
        self.cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))
        self.conn.commit()
        print(f"Contato '{nome}' removido com sucesso.")

    def buscar_contato(self, nome):
        """Busca um contato na agenda."""
        self.cursor.execute("SELECT endereco, data_nascimento, telefones, emails FROM contatos WHERE nome = ?", (nome,))
        resultado = self.cursor.fetchone()
        if resultado:
            endereco, data_nascimento, telefones, emails = resultado
            return {
                "endereco": endereco,
                "data_nascimento": data_nascimento,
                "telefones": telefones.split(","),
                "emails": emails.split(",")
            }
        return f"Contato '{nome}' não encontrado."

    def listar_contatos(self):
        """Lista todos os contatos na agenda."""
        self.cursor.execute("SELECT nome, endereco, data_nascimento, telefones, emails FROM contatos")
        contatos = self.cursor.fetchall()
        if not contatos:
            print("A agenda está vazia.")
        else:
            for nome, endereco, data_nascimento, telefones, emails in contatos:
                print(f"Nome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_nascimento}\nTelefones: {telefones}\nEmails: {emails}\n")

    def __del__(self):
        self.conn.close()

def menu():
    agenda = Agenda()
    while True:
        print("\nAgenda Telefônica")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Listar contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            endereco = input("Endereço (Rua, Número, Complemento, Bairro, Município, Estado, CEP): ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            telefones = input("Telefones (separados por vírgula): ").split(",")
            emails = input("Emails (separados por vírgula): ").split(",")
            agenda.adicionar_contato(nome, endereco, data_nascimento, telefones, emails)
        elif opcao == "2":
            nome = input("Nome do contato a remover: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Nome do contato a buscar: ")
            print(agenda.buscar_contato(nome))
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
