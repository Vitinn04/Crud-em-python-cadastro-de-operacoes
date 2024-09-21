# Abra o terminal e escreva "pip install mysql-connector-python"

import mysql.connector

# Abra o Workbench e crie uma database e a tabela que vai usar (estão na pasta "Banco de dados")

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

# função para dar update em alguma operação
def alterarOp():
    op = input("Qual operação deseja alterar (para ver as operações rode a função de ver operções)? EX: 1 ")
    mudar = str(input("Qual campo deseja alterar na tabela [ 1 ] Nome da Operação, [ 2 ] Quantidade de policias, [ 3 ] Local da operação, [ 4 ] Data da operação, [ 5 ] Descrição da operação: "))

    if mudar == "1":
        mudar = "nomeOp"
    elif mudar == "2":
        mudar = "qtdPoliciais"
    elif mudar == "3":
        mudar = "localOp"
    elif mudar == "4":
        mudar = "dataOp"
    elif mudar == "5":
        mudar = "descricaoOp"
    else:
        print("Valor invalido tente novamente")
        alterarOp()

    alterado = input(f"Digite o/a {mudar}: ")

    comando = f'UPDATE operacoes SET {mudar} = "{alterado}" WHERE codigoOp = {op};'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (Insert, Update, Delete)

    comando = f'SELECT * FROM operacoes WHERE codigoOp = {op};'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (Select)
    print(f"\nO valor alterado na tabela: {resultado}\n")

# função para deletar alguma operação
def deletarOp():
    op = input("\nQual operação deseja deletar (para ver as operações rode a função de ver operções)? EX: 1 ")

    comando = f'DELETE FROM operacoes WHERE codigoOp = {op};'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (Insert, Update, Delete)

    print(f"\nA operação com o ID {op} foi deletada\n")

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
