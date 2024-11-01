# Entre com uma lista de alunos e notas (n1 e n2) terminada com nome igual a 'fim'
# Mostrar as médias dos alunos
# Mostrar os alunos aprovados e em prova final (media >= 6 para aprovação)

'''
nomes = ["Andre", "Bruno", "Carlos", "Eloisa"]
notas1 = [6, 7, 8, 9]
notas2 = [9, 8, 7, 6]
'''
MIN_TAM_NOME = 4
MEDIA_APROVACAO = 6
FLAG = 'fim'

def entrar_nome():
    while True:
        nome = input('Entre com o nome: ')
        if len(nome) < MIN_TAM_NOME:
            print('Erro: nome inválido')
        else:
            break
    return nome

def entrar_nota(msg):
    while True:
        try:
            nota = float(input(msg))
            break
        except:
            print('Erro: nota inválida')
    return nota

def entrar_alunos():
    turma = []
    nome = entrar_nome()
    while nome.lower() != FLAG:
        n1 = entrar_nota('Entre com a nota 1: ')
        n2 = entrar_nota('Entre com a nota 2: ')
        aluno = [nome, n1, n2]
        turma.append(aluno)
        nome = input('Entre com o nome: ')
    return turma

def exibir_turma(turma):
    for aluno in turma:
        print(aluno)

def calcular_medias(turma):
    medias = []
    for aluno in turma:
        media = (aluno[1] + aluno[2]) / 2
        medias.append([aluno[0], media])
    return medias

def exibir_medias(medias):
    for media in medias:
        print(f'Nome: {media[0]} - Média: {media[1]:.2f}')

def exibir_aprovacao(medias):
    for aluno in medias:
        if aluno[1] >= MEDIA_APROVACAO:
            print(f'{aluno[0]} está aprovado')
        else:
            print(f'{aluno[0]} está em prova final')


#Usando lista de listas
#turma = [['Andre', 7, 9], ['Bruno', 7, 8], ['Carlos', 8, 7], ['Eloisa', 5, 6]]

'''for i in range(len(turma)):
    print(turma[i])'''

#exibir_turma(turma)

turma = entrar_alunos()
medias = calcular_medias(turma)
exibir_medias(medias)
exibir_aprovacao(medias)
