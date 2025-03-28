import pandas as pd
from conectar_db import *

def ler_turma_sql():
    sql = "SELECT * FROM aluno"
    try:
        conn = conectar()
        cursor = conn.cursor() # cria um cursor para percorrer o banco de dados
        cursor.execute(sql)
        registros = cursor.fetchall()
        turma = []
        for registro in registros:
            turma.append([int(registro[0]), registro[1], float(registro[2]), float(registro[3])])
            #explicação: registro[0] é o id, registro[1] é o nome, registro[2] é a nota1 e registro[3] é a nota2
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return turma

def ler_turma_pandas():
    conn = conectar()
    sql = "SELECT * FROM aluno"
    df = pd.read_sql_query(sql, conn)
    desconectar(conn)
    return df

def verificar_aprovação(df):
    '''
    df['media'] = (df['nota1'] + df['nota2']) / 2
    df['aprovado'] = df['media'] >= 7
    print(df)
    '''
    df_aprovacao = pd.DataFrame(columns=['nome', 'media', 'status'])
    for _ , aluno in df.iterrows(): # _ é o índice da linha. para cada linha do dataframe
        media = (aluno['nota1'] + aluno['nota2']) / 2
        if (media >=6):
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Aprovado']
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'ProvaFinal']

    return df_aprovacao



turma = ler_turma_sql()
print(turma)

df_turma = ler_turma_pandas()
print(df_turma)

# Consultas com pandas

# 1. Verificar a aprovação dos alunos

df_aprovacao = verificar_aprovação(df_turma)
print(df_aprovacao)