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

# função para dar o insert
def criarOp():
    nomeOp = str(input("\nNome da Operação: "))
    qtdPoliciais = int(input("Quantidade de policias nescessários: "))
    localOp = str(input("Local da operação: "))
    dataOp = input("Data da operação: ")
    descricaoOp = str(input("Descrição da operação: \n"))

    comando = f'INSERT INTO operacoes (nomeOp, qtdPoliciais, localOp, dataOp, descricaoOp) VALUES ("{nomeOp}", {qtdPoliciais}, "{localOp}", "{dataOp}", "{descricaoOp}");'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados (Insert, Update, Delete)

# função para ver as operações já cadastradas
def verOp():
    comando = f'SELECT * FROM operacoes;'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados (Select)
    print(f"\nOs valores da tabela: {resultado}\n")

def alterarOp():
    comando = f""

def deletarOp():
    comando = f""

while True:
    escolha = int(input("Deseja rodar qual função?? \n[ 1 ] = Criar operação \n[ 2 ] = Ver operações \n[ 3 ] = Alterar operação \n[ 4 ] = Deletar operação \n[ 5 ] = Sair \nDigite a sua escolha: "))
    # roda a função
    if escolha == 1:
        criarOp()
    elif escolha == 2:
        verOp()
    elif escolha == 3:
        alterarOp()
    elif escolha == 4:
        deletarOp()
    elif escolha == 5:
        break
    else:
        escolha = int(input("Valor inválido!!! Deseja rodar qual função?? \n[ 1 ] = Criar operação \n[ 2 ] = Ver operações \n[ 3 ] = Alterar operação \n[ 4 ] = Deletar operação \n[ 5 ] = Sair \nDigite a sua escolha: "))


# fecha a conexão
cursor.close()
conexao.close()
