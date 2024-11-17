import time
from datetime import datetime

tarefas = []

def validar_data():
    """
    Valida a data de prazo final da tarefa. A data deve ser fornecida no formato DD-MM-YYYY.

    Returns:
        str: A data validada no formato DD-MM-YYYY.
    """
    while True:
        prazo_final = input('Digite o prazo final da tarefa (formato DD-MM-YYYY): ')
        try:
            datetime.strptime(prazo_final, '%d-%m-%Y')
            break  
        except ValueError:
            print('Formato inválido! Digite a data no formato DD-MM-YYYY.')
    return prazo_final

def validar_urgencia():
    """
    Valida o nível de urgência da tarefa. A entrada deve ser 'alta', 'média' ou 'baixa'.

    Returns:
        str: O nível de urgência validado.
    """
    while True:
        urgencia = input('Digite o nível de urgência (alta, média, baixa): ').strip().lower()
        if urgencia in ["alta", "média", "baixa"]:
            break
        else:
            print('Valor inválido! Digite alta, média ou baixa.')
    return urgencia

def gerar_id_tarefa():
    """
    Gera um ID único para a tarefa. O ID será o maior ID existente + 1,
    ou 1 se a lista de tarefas estiver vazia.

    Returns:
        int: O ID único gerado.
    """
    if tarefas:
        maior_id = max(tarefa[0] for tarefa in tarefas)
        return maior_id + 1
    else:
        return 1

def data_atual():
    """
    Obtém a data atual no formato DD-MM-YYYY.

    Returns:
        str: A data atual no formato DD-MM-YYYY.
    """
    return datetime.now().strftime('%d-%m-%Y')    

def adicionar_tarefa():
    """
    Adiciona uma nova tarefa à lista de tarefas. Solicita descrição, prazo final e nível de urgência.

    Returns:
        None
    """
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
    print('Tarefa adicionada com sucesso!')

def exibir_tarefas():
    """
    Exibe todas as tarefas cadastradas com suas informações.

    Returns:
        None
    """
    print('-' * 40)
    if len(tarefas) == 0:
        print('Lista Vazia')
    else:
        print('Tarefas cadastradas:')
        for tarefa in tarefas:
            status = '(concluída)' if tarefa[3] == "concluída" else '(pendente)'
            print(f'ID: {tarefa[0]} - {tarefa[1]} - {status}')
            print(f'Data de criação: {tarefa[2]}, Prazo: {tarefa[4]}, Urgência: {tarefa[5]}')
            print('-' * 40)
    time.sleep(2)

def encontrar_tarefa_por_id():
    """
    Localiza uma tarefa pelo ID fornecido pelo usuário.

    Returns:
        tuple: Um par contendo o índice da tarefa e a própria tarefa, ou (None, None) se não encontrada.
    """
    try:
        tarefa_id = int(input('Digite o ID da tarefa: '))
        for i, tarefa in enumerate(tarefas):
            if tarefa[0] == tarefa_id:
                return i, tarefa
        print('Tarefa não encontrada.')
    except ValueError:
        print('Erro! Digite um número inteiro válido.')
    
    return None, None

def verificar_tarefa_ja_concluida(tarefa):
    """
    Verifica se uma tarefa já está concluída.

    Args:
        tarefa (list): A tarefa a ser verificada.

    Returns:
        bool: True se a tarefa já estiver concluída, False caso contrário.
    """
    return tarefa[3] == "concluída"

def marcar_tarefa_como_concluida():
    """
    Marca uma tarefa como concluída.

    Returns:
        None
    """
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        index, tarefa = encontrar_tarefa_por_id()
        if tarefa:
            if verificar_tarefa_ja_concluida(tarefa):
                print('A tarefa já está marcada como concluída.')
            else:
                tarefa[3] = "concluída"
                print('Tarefa marcada como concluída!')

def remover_tarefa():
    """
    Remove uma tarefa da lista com base no ID fornecido.

    Returns:
        None
    """
    exibir_tarefas()
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada, não é possível remover.')
    else:
        index, tarefa = encontrar_tarefa_por_id()
        if tarefa:
            tarefas.pop(index)
            print('Tarefa removida com sucesso!')

def menu():
    """
    Exibe o menu de opções e executa a função correspondente à escolha do usuário.

    Returns:
        None
    """
    while True:
        try:
            print('Menu de opções')
            print('1 - Adicionar tarefa')
            print('2 - Exibir tarefas')
            print('3 - Marcar tarefa como concluída')
            print('4 - Remover tarefa')
            print('5 - Sair')
            opcao = int(input('Digite a opção: '))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                exibir_tarefas()
            elif opcao == 3:
                marcar_tarefa_como_concluida()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                print("Saindo...")
                break
            else:
                print('ERRO! Opção Inválida! Tente novamente')
        except ValueError:
            print('ERRO! Entre com um número inteiro')

menu()