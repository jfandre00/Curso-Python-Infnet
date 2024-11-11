import os
import time
from datetime import datetime

tarefas = []

def validar_data():
    '''
    Função para validar a data de prazo final da tarefa.
    A data deve ser no formato DD-MM-YYYY.
    '''
    while True:
        prazo_final = input('Digite o prazo final da tarefa (formato DD-MM-YYYY): ')
        try:
            datetime.strptime(prazo_final, '%d-%m-%Y')
            break  
        except ValueError:
            print('\033[1;4;91mFormato inválido! Digite a data no formato DD-MM-YYYY.\033[0m')
    return prazo_final

def validar_urgencia():
    '''
    Função para validar a urgência da tarefa.
    A urgência deve ser alta, média ou baixa.
    '''
    while True:
        urgencia = input('Digite o nível de urgência (alta, média, baixa): ').strip().lower()
        if urgencia in ["alta", "média", "baixa"]:
            break
        else:
            print('\033[1;4;91mValor inválido! Digite alta, média ou baixa.\033[0m')
    return urgencia

def gerar_id_tarefa():
    '''
    Função para gerar um ID único para a tarefa.
    O ID é o maior ID existente + 1, ou 1 se a lista de tarefas estiver vazia.
    '''

    if tarefas:
        maior_id = max(tarefa[0] for tarefa in tarefas)  # Encontra o maior ID existente
        return maior_id + 1
    else:
        return 1  # Se a lista estiver vazia, inicia do ID 1

def data_atual():
    '''
    Função para retornar a data atual no formato DD-MM-YYYY.
    '''
    return datetime.now().strftime('%d-%m-%Y')    

def adicionar_tarefa():
    '''
    Função para adicionar uma tarefa à lista de tarefas.
    A tarefa inclui uma descrição, data de criação, prazo final e urgência.
    '''
    descricao = input('Digite a descrição da tarefa: ')
    
    prazo_final = validar_data()

    urgencia = validar_urgencia()
    
    id_tarefa = gerar_id_tarefa()

    data_criacao = data_atual()

    tarefa_a_adicionar = [
        id_tarefa,        # ID
        descricao,        # Descrição
        data_criacao,     # Data de Criação
        "pendente",       # Status inicial
        prazo_final,      # Prazo final
        urgencia          # Nível de urgência
    ]

    tarefas.append(tarefa_a_adicionar)
    os.system('cls')
    print('\033[1;34m\033[1mTarefa adicionada com sucesso!\033[0m')

def exibir_tarefas():
    '''
    Função para exibir as tarefas cadastradas com seus metadados.
    '''
    os.system('cls')
    print('-' * 40)
    if len(tarefas) == 0:
        print('Lista Vazia')
    else:
        print('Tarefas cadastradas:')
        for tarefa in tarefas:
            status = '\033[1;34m(concluída)\033[0m' if tarefa[3] == "concluída" else '\033[1;35m(pendente)\033[0m'
            print(f'ID: {tarefa[0]} - {tarefa[1]} - {status}')
            print(f'Data de criação: {tarefa[2]}, Prazo: {tarefa[4]}, Urgência: {tarefa[5]}')
            print('-' * 40)
    time.sleep(2) # Aguarda 2 segundos para exibir as tarefas

def encontrar_tarefa_por_id():
    '''
    Função para encontrar uma tarefa pelo ID fornecido pelo usuário.
    Solicita o ID, valida a entrada e retorna o índice e a tarefa.
    Retorna (None, None) se o ID não for encontrado ou se a entrada for inválida.
    '''
    try:
        tarefa_id = int(input('Digite o ID da tarefa: '))
        for i, tarefa in enumerate(tarefas):
            if tarefa[0] == tarefa_id:  # ID é o primeiro elemento na lista de cada tarefa
                return i, tarefa
        print('\033[1;4;91mTarefa não encontrada.\033[0m')
    except ValueError:
        print('\033[1;4;91mErro! Digite um número inteiro válido.\033[0m')
    
    return None, None  # Retorna None se o ID não for encontrado ou a entrada for inválida

def verificar_tarefa_ja_concluida(tarefa):
    '''
    Função para verificar se uma tarefa já está marcada como concluída.
    Retorna True se a tarefa já estiver concluída, caso contrário, False.
    '''
    return tarefa[3] == "concluída"

def marcar_tarefa_como_concluida():
    '''
    Função para marcar uma tarefa como concluída.
    '''
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        index, tarefa = encontrar_tarefa_por_id()
        if tarefa:
            if verificar_tarefa_ja_concluida(tarefa):
                print('\033[1;4;93mA tarefa já está marcada como concluída.\033[0m')
            else:
                tarefa[3] = "concluída"
                os.system('cls')
                print('\033[1;34m\033[1mTarefa marcada como concluída!\033[0m')

def remover_tarefa():
    '''
    Função para remover uma tarefa da lista.
    '''
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada, não é possível remover.')
    else:
        index, tarefa = encontrar_tarefa_por_id()
        if tarefa:
            tarefas.pop(index)
            os.system('cls')
            print('\033[1;34m\033[1mTarefa removida com sucesso!\033[0m')

def menu():
    '''
    Função para exibir o menu de opções, que chama as funções de acordo com a opção escolhida e trata exceções
    Exibe o menu até que o usuário escolha a opção de sair, e as opções estão coloridas.
    '''
    while True:
        try:
            print('\033[1;4;92mMenu de opções\033[0m')
            print('\033[92m1\033[0m - Adicionar tarefa')
            print('\033[92m2\033[0m - Exibir tarefas')
            print('\033[92m3\033[0m - Marcar tarefa como concluída')
            print('\033[92m4\033[0m - Remover tarefa')
            print('\033[92m5\033[0m - Sair')
            opcao = int(input('\033[1;4;92mDigite a opção:\033[0m '))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                exibir_tarefas()
            elif opcao == 3:
                marcar_tarefa_como_concluida()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                break
            else:
                print('\033[1;4;91mERRO! Opção Inválida! Tente novamente\033[0m')
        except ValueError:
            print('\033[1;4;91mERRO! Entre com um número inteiro\033[0m')

menu()
