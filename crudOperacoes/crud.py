# Abra o terminal e escreva "pip install mysql-connector-python"

import mysql.connector

# Abra o Workbench e crie uma database e a tabela que vai usar

# Crie a conexão com o banco criado no workbench
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='25117195',
    database='crudOp',
)

# criar um cursor (executa os comandos da conexão)
cursor = conexao.cursor()

escolha = int(input("Deseja rodar qual função?? [ 1 ] = Criar operação ou [ 2 ] = Ver operações: "))

# função para dar o insert
def criarOp():
    nomeOp = str(input("Nome da Operação: "))
    qtdPoliciais = int(input("Quantidade de policias nescessários: "))
    localOp = str(input("Local da operação: "))
    dataOp = input("Data da operação: ")
    descricaoOp = str(input("Descrição da operação: "))

    comando = f'INSERT INTO operacoes (nomeOp, qtdPoliciais, localOp, dataOp, descricaoOp) VALUES ("{nomeOp}", {qtdPoliciais}, "{localOp}", "{dataOp}", "{descricaoOp}");'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados (Insert, Update, Delete)

# função para ver as operações já cadastradas
def verOp():
    comando = f'SELECT * FROM operacoes;'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados (Select)
    print(resultado)

# roda a função
if escolha == 1:
    criarOp()
elif escolha == 2:
    verOp()

# fecha a conexão
cursor.close()
conexao.close()
