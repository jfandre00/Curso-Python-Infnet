#TP3 - Agenda Telefônica com SQLite e CRUD - André Loureiro Montini Ferreira
#Instituto INFNET - 2025

'''No enunciado do TP3, o professor Luiz solicitou a criação de uma agenda telefônica, 
sugerindo o uso de dicionários e listas ou SQLite. Optei por utilizar SQLite para uma 
melhor estruturação dos dados e persistência.

Quanto ao campo de endereço, poderia ter sido dividido em múltiplos campos, 
mas preferi manter um único campo para simplificar o design da agenda.'''


import sqlite3
import os

'''
Regra de Negócio: Não é permitido alterar o nome de um contato. 
Caso o usuário queira alterar o nome, será necessário remover o contato com o nome antigo e adicionar um novo com o nome alterado.
'''


# ==============================================================================================#
#                                    Classe Agenda                                              #
# Responsável por gerenciar os contatos da agenda utilizando um banco de dados SQLite.          #
# Fornece métodos para adicionar, remover, buscar, listar e alterar contatos.                   #
# Os métodos tem tratamento de exceções para lidar com erros de conexão com o banco de dados.   #
# ==============================================================================================#

class Agenda:
    def __init__(self): #construtor (método que é chamado quando a classe é instanciada)
        try:
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
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}") 

    def adicionar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        '''
        Adiciona um contato na agenda.

        Parâmetros:
        nome (str): Nome do contato a ser adicionado.
        endereco (str): Endereço do contato.
        data_nascimento (str): Data de nascimento do contato.
        telefones (list): Lista de telefones do contato.
        emails (list): Lista de emails do contato.

        Retorno:
        Nenhum.
        '''
        try:
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
        except sqlite3.Error as e:
            print(f"Erro ao adicionar contato: {e}")

    def remover_contato(self, nome):
        '''
        Remove um contato da agenda.

        Parâmetros:
        nome (str): Nome do contato a ser removido.

        Retorno:
        Nenhum.
        '''
        try:
            self.cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))
            if self.cursor.rowcount == 0:
                print(f"Erro: Contato '{nome}' não encontrado.")
            else:
                self.conn.commit()
                print(f"Contato '{nome}' removido com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao remover contato: {e}")

    def buscar_contato(self, nome):
        '''
        Busca um contato na agenda.

        Parâmetros:
        nome (str): Nome do contato a ser buscado.

        Retorno:
        str: Informações do contato encontrado ou mensagem de erro caso o contato não seja encontrado.
        '''
        try:
            self.cursor.execute("SELECT endereco, data_nascimento, telefones, emails FROM contatos WHERE nome = ?", (nome,))
            resultado = self.cursor.fetchone()
            if resultado:
                endereco, data_nascimento, telefones, emails = resultado
                return f"\nNome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_nascimento}\nTelefones: {telefones}\nEmails: {emails}"
            return f"Contato '{nome}' não encontrado."
        except sqlite3.Error as e:
            return f"Erro ao buscar contato: {e}"

    def listar_contatos(self):
        '''
        Lista todos os contatos da agenda.

        Parâmetros:
        Nenhum.

        Retorno:
        Nenhum.
        '''
        try:
            self.cursor.execute("SELECT nome, endereco, data_nascimento, telefones, emails FROM contatos")
            contatos = self.cursor.fetchall()
            if not contatos:
                print("A agenda está vazia.")
            else:
                for idx, (nome, endereco, data_nascimento, telefones, emails) in enumerate(contatos, start=1):
                    print(f"{idx}. Nome: {nome}\nEndereço: {endereco}\nData de Nascimento: {data_nascimento}\nTelefones: {telefones}\nEmails: {emails}\n")
        except sqlite3.Error as e:
            print(f"Erro ao listar contatos: {e}")


    def alterar_contato(self, nome, endereco, data_nascimento, telefones, emails):
        '''
        Altera um contato na agenda.

        Parâmetros:
        nome (str): Nome do contato a ser alterado.
        endereco (str): Novo endereço do contato.
        data_nascimento (str): Nova data de nascimento do contato.
        telefones (list): Novos telefones do contato.
        emails (list): Novos emails do contato.

        Retorno:
        Nenhum.
        '''
        try:
            self.cursor.execute("SELECT nome FROM contatos WHERE nome = ?", (nome,))
            if not self.cursor.fetchone():
                print(f"Erro: Contato '{nome}' não encontrado.")
                return

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
        except sqlite3.Error as e:
            print(f"Erro ao alterar contato: {e}")


    def fechar_conexao(self):
        '''
        Método para fechar a conexão com o banco de dados.

        Parâmetros:
        Nenhum.

        Retorno:
        Nenhum.
        '''
        try:
            self.conn.close()
            print("Conexão com o banco de dados fechada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao fechar conexão com o banco de dados: {e}")

# =======================================================================
# Funções auxiliares para interação com a classe Agenda
# Essas funções servem como intermediárias para facilitar a interação 
# do usuário com os métodos da classe Agenda no menu principal.
# =======================================================================

def alterar_dado_contato(agenda, escolher_qual_dado_alterar):
    '''
    Função que altera um dado de um contato na agenda. Atenção: o nome do contato é a chave primária, ou seja, não pode ser alterado.

    Parâmetros:
    agenda (Agenda): Instância da classe Agenda.
    escolher_qual_dado_alterar (str): Opção escolhida pelo usuário para alterar um dado do contato.

    Retorno:
    Nenhum.
    '''
    nome = input("Nome do contato a alterar: ")
    #verificar se o contato existe
    agenda.cursor.execute("SELECT nome FROM contatos WHERE nome = ?", (nome,))
    resultado = agenda.cursor.fetchone()
    if not resultado:
        print(f"Contato '{nome}' não encontrado.")
        return
    #Adicionei validação para garantir que o campo de endereço, data de nascimento, telefones e emails não sejam vazios.
    if escolher_qual_dado_alterar == "1":
        endereco = input("Endereço: ").strip()
        if endereco:
            agenda.alterar_contato(nome, endereco, None, None, None)
        else:
            print("Erro: O campo de endereço não pode ser vazio.")
    elif escolher_qual_dado_alterar == "2":
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()
        if data_nascimento:
            agenda.alterar_contato(nome, None, data_nascimento, None, None)
        else:
            print("Erro: O campo de data de nascimento não pode ser vazio.")
    elif escolher_qual_dado_alterar == "3":
        telefones = [telefone.strip() for telefone in input("Telefones (separados por vírgula): ").split(",") if telefone.strip()]
        if telefones:
            agenda.alterar_contato(nome, None, None, telefones, None)
        else:
            print("Erro: O campo de telefones não pode ser vazio.")
    elif escolher_qual_dado_alterar == "4":
        emails = [email.strip() for email in input("Emails (separados por vírgula): ").split(",") if email.strip()]
        if emails:
            agenda.alterar_contato(nome, None, None, None, emails)
        else:
            print("Erro: O campo de emails não pode ser vazio.")
    else:
        print("Opção inválida. Tente novamente.")

def obter_dados_do_usuario(agenda, nome):
    '''
    Função que obtém os dados do usuário para adicionar um contato na agenda. Garante que os campos obrigatórios não sejam vazios.

    Parâmetros:
    agenda (Agenda): Instância da classe Agenda.
    nome (str): Nome do contato a ser adicionado.

    Retorno:
    Nenhum.
    '''
    while True:
        endereco = input("Endereço Completo: ").strip()
        if endereco:
            break
        else:
            print("Erro: O campo de endereço não pode ser vazio.")
    
    while True:
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ").strip()
        if data_nascimento:
            break
        else:
            print("Erro: O campo de data de nascimento não pode ser vazio.")
    
    while True:
        telefones = [telefone.strip() for telefone in input("Telefones (separados por vírgula): ").split(",") if telefone.strip()]
        if telefones:
            break
        else:
            print("Erro: O campo de telefones não pode ser vazio.")
    
    while True:
        emails = [email.strip() for email in input("Emails (separados por vírgula): ").split(",") if email.strip()]
        if emails:
            break
        else:
            print("Erro: O campo de emails não pode ser vazio.")
    agenda.adicionar_contato(nome, endereco, data_nascimento, telefones, emails)

# =======================================================================
# Função principal do programa
# O menu fornece uma interface interativa para o usuário manipular a agenda.
# =======================================================================
    
def menu():
    '''
    Função que exibe o menu de opções para o usuário interagir com a agenda.
    O usuário pode adicionar, remover, buscar, listar e alterar contatos.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    '''
    agenda = Agenda() #instancia a classe Agenda
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
            while True: #loop para garantir que o campo de nome não seja vazio
                nome = input("Nome: ").strip() 
                if nome:
                    break
                else:
                    print("Erro: O campo de nome não pode ser vazio.")
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

'''Usando 'if __name__ == "__main__"' para garantir que o menu seja executado apenas quando o script for executado diretamente
   E não quando o módulo for importado em outro arquivo.'''

if __name__ == "__main__":
    menu()
