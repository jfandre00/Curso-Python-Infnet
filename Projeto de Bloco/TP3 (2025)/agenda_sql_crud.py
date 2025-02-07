#TP3 - Agenda Telefônica com SQLite e CRUD - André Loureiro Montini Ferreira
#Instituto INFNET - 2025

'''No enunciado do TP3, o professor Luiz pediu para criarmos uma agenda telefônica, poderia utilizar dicionários e listas OU SQLite. Preferi utilizar SQLite.
No endereço poderia ter feito vários campos separados, mas preferi fazer um campo só, para simplificar'''

import sqlite3
import os

#Consideração: Optei por criar uma classe para a agenda para manter o código mais organizado. Com isso, todas as funções da agenda se tornam métodos da classe, eliminando a necessidade de passar a agenda como parâmetro para todas as funções. Além disso, essa abordagem facilita a reutilização da classe em outros projetos, se necessário.
#(Regra de Negócio) Se o usuário quiser alterar o nome de um contato, ele terá que remover o contato e adicionar um novo com o nome alterado.


class Agenda:
    def __init__(self): #construtor (método que é chamado quando a classe é instanciada)
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "agenda.db"))
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                --eu sei que poderia ter feito um id autoincrement, mas preferi usar o nome como chave primária, para ser diferente do exemplo que o professor Luiz fez em aula (assim eu pratico outras formas de fazer)
                nome TEXT PRIMARY KEY,
                endereco TEXT,
                data_nascimento TEXT,
                telefones TEXT,
                emails TEXT
            )
        ''')
        self.conn.commit() #salva as alterações no banco de dados

    def adicionar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        """Adiciona um contato na agenda."""
        #transformar listas em strings separadas por vírgula
        telefones_str = ",".join(telefones) 
        emails_str = ",".join(emails)
        self.cursor.execute("""
            INSERT INTO contatos (nome, endereco, data_nascimento, telefones, emails) 
            VALUES (?, ?, ?, ?, ?) 
            --ON CONFLICT(nome) DO UPDATE SET endereco=excluded.endereco, data_nascimento=excluded.data_nascimento, telefones=excluded.telefones, emails=excluded.emails
            --removi o ON CONFLICT, pois não queria que o contato fosse atualizado caso já existisse, criei uma função específica para alterar o contato
        """, (nome, endereco, data_nascimento, telefones_str, emails_str))
        self.conn.commit()
        print(f"Contato '{nome}' adicionado com sucesso.")

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
            return f"\nNome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_nascimento}\nTelefones: {telefones}\nEmails: {emails}"
        return f"Contato '{nome}' não encontrado."

    def listar_contatos(self):
        """Lista todos os contatos na agenda."""
        self.cursor.execute("SELECT nome, endereco, data_nascimento, telefones, emails FROM contatos")
        contatos = self.cursor.fetchall()
        if not contatos:
            print("A agenda está vazia.")
        else:
            for idx, (nome, endereco, data_nascimento, telefones, emails) in enumerate(contatos, start=1):
                print(f"{idx}. Nome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_nascimento}\nTelefones: {telefones}\nEmails: {emails}\n")

    def alterar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        """Altera um contato na agenda."""
        if endereco:
            self.cursor.execute("UPDATE contatos SET endereco = ? WHERE nome = ?", (endereco, nome))
        if data_nascimento:
            self.cursor.execute("UPDATE contatos SET data_nascimento = ? WHERE nome = ?", (data_nascimento, nome))
        if telefones:
            telefones_str = ",".join(telefones)
            self.cursor.execute("UPDATE contatos SET telefones = ? WHERE nome = ?", (telefones_str, nome))
        if emails:
            emails_str = ",".join(emails)
            self.cursor.execute("UPDATE contatos SET emails = ? WHERE nome = ?", (emails_str, nome))
        self.conn.commit()
        print(f"Contato '{nome}' alterado com sucesso.")

    def __del__(self):
        self.conn.close()

    def fechar_conexao(self):
        self.conn.close()

def alterar_dado_contato(agenda, escolher_qual_dado_alterar):
    '''
    Função que altera um dado de um contato na agenda. Atenção: o nome do contato é a chave primária, ou seja, não pode ser alterado.
    '''
    nome = input("Nome do contato a alterar: ")
    #verificar se o contato existe
    agenda.cursor.execute("SELECT nome FROM contatos WHERE nome = ?", (nome,))
    resultado = agenda.cursor.fetchone()
    if not resultado:
        print(f"Contato '{nome}' não encontrado.")
        return
    if escolher_qual_dado_alterar == "1":
        endereco = input("Endereço: ")
        agenda.alterar_contato(nome, endereco, None, None, None)
    elif escolher_qual_dado_alterar == "2":
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        agenda.alterar_contato(nome, None, data_nascimento, None, None)
    elif escolher_qual_dado_alterar == "3":
        telefones = input("Telefones (separados por vírgula): ").split(",")
        agenda.alterar_contato(nome, None, None, telefones, None)
    elif escolher_qual_dado_alterar == "4":
        emails = input("Emails (separados por vírgula): ").split(",")
        agenda.alterar_contato(nome, None, None, None, emails)
    else:
        print("Opção inválida. Tente novamente.")

def obter_dados_do_usuario(agenda, nome):
    '''
    Função que obtém os dados do usuário para adicionar um contato na agenda.
    '''
    endereco = input("Endereço Completo: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    telefones = input("Telefones (separados por vírgula): ").split(",")
    emails = input("Emails (separados por vírgula): ").split(",")
    agenda.adicionar_contato(nome, endereco, data_nascimento, telefones, emails)
    
def menu():
    agenda = Agenda()
    while True:
        print("\nAgenda Telefônica v1.0")
        print("---------Menu de Opções---------")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Listar contatos")
        print("5. Alterar dado(s) de um contato")
        print("6. Sair")
        print("-------------------------------")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            #Validação: não permitir que o usuário adicione um contato que já exista
            agenda.cursor.execute("SELECT nome FROM contatos WHERE nome = ?", (nome,))
            resultado = agenda.cursor.fetchone()
            if resultado:
                print(f"Contato '{nome}' já existe. Use a opção 5 para alterar o contato.")
                continue
            obter_dados_do_usuario(agenda, nome)
        elif opcao == "2":
            nome = input("Nome do contato a remover: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Nome do contato a buscar: ")
            print(agenda.buscar_contato(nome))
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            escolher_qual_dado_alterar = input("Qual dado deseja alterar?\n 1.Endereço\n 2.Data de Nascimento\n 3.Telefone(s)\n 4.Email(s): ")
            if escolher_qual_dado_alterar in ["1", "2", "3", "4"]:
                alterar_dado_contato(agenda, escolher_qual_dado_alterar)
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == "6":
            #vamos fechar a conexao com o banco de dados aqui, já que o programa vai encerrar.
            agenda.fechar_conexao()
            print("Saindo...\nObrigado por usar a Agenda Telefônica v1.0")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
