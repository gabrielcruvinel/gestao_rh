import sqlite3
import os
from sqlite3 import Error


def Menu():
    print("*******Livraria*******\n")
    print("1 => Criar banco de dados")
    print("2 => Cadastrar Cliente")
    print("3 => Mostrar todos os Clientes")
    print("4 => Deletar Cliente")
    print("5 => Alterar Cadastro de Cliente")
    print("0 => Sair\n")
    escolha = int(input("Digite a opção desejada:"))
    while escolha != 0:
        if escolha == 1:
            createTable()
        elif escolha == 2:
            nome = input("Digite o nome do Cliente:")
            telefone = int(input("Digite o telefone do Cliente:"))
            cpf = input("Digite o cpf do Cliente")
            insertValue(nome, telefone, cpf)
        elif escolha == 3:
            showAll()
        elif escolha == 4:
            nome = input("Digite o nome do Cliente a ser excluído:")
            delete(nome)
        elif escolha == 5:
            nome = input("Digite o nome do Cliente a ser modificado:")
            update(nome)
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu()
def update(nome):
    database = 'livraria.db'
    conexao=sqlite3.connect(database)
    print("================= ALTERAÇÃO DE CADASTRO =================")
    print("1 =>         ALTERAR NOME DO CLIENTE")
    print("2 =>         ALTERAR NUMERO DO CLIENTE")
    print("3 =>         ALTERAR CPF DO CLIENTE")
    escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?"))
    if escolha == 1:
        query = "UPDATE cliente SET nome=?"
        try:
            cur=conexao.cursor()
            nome = input("Digite o Nome do Cliente:")
            cur.execute(query,(nome,))
            conexao.commit()
            print("Nome alterado com sucesso")
        except:
            print("Erro ao alterar campo")
        cur.close()
        conexao.close()
    elif escolha == 2:
        query = "UPDATE cliente SET telefone=?"
        try:
            cur=conexao.cursor()
            telefone = int(input("Digite o telefone do Cliente"))
            cur.execute(query,(telefone,))
            conexao.commit()
            print("Telefone alterado com sucesso")
        except:
            print("Erro ao alterar campo")
        cur.close()
        conexao.close()
    elif escolha == 3:
        query = "UPDATE cliente set cpf=?"
        try:
            cur=conexao.cursor()
            cpf = input("Digite o cpf do Cliente")
            cur.execute(query,(cpf,))
        except:
            print("Erro ao alterar campo")
        cur.close()
        conexao.close()
def delete(nome):
    database = 'livraria.db'
    conexao=sqlite3.connect(database)
    query = "DELETE FROM cliente WHERE nome=?"
    try:
        cur=conexao.cursor()
        cur.execute(query,(nome,))
        conexao.commit()
        print("Cliente Deletado com Sucesso")
        input()
    except:
        print("Erro ao Deletar Cliente")
    cur.close()
    conexao.close()
def createTable():
    database = 'livraria.db'
    conexao=sqlite3.connect(database)
    try:
        cur=conexao.cursor()
        cur.execute('''CREATE TABLE if not exists cliente(id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome NOT NULL, 
         telefone INTEGER, 
         cpf TEXT)''')
        conexao.commit()
        print("Tabela criada com Sucesso!")
        input()

    except Error as e:
        print("Erro:")
        print(e)
        conexao.rollback()
    cur.close()
    conexao.close()
def insertValue(nome, telefone, cpf):
    database = 'livraria.db'
    conexao=sqlite3.connect(database)
    query = '''INSERT INTO cliente (nome, telefone, cpf) VALUES (?, ?, ?)'''
    try:
        cur=conexao.cursor()
        cur.execute(query,(nome, telefone, cpf))
        conexao.commit()
        print("Cliente cadastrado com sucesso")
    except:
        print("Erro ao adicionar cliente")
    cur.close()
    conexao.close()
def showAll():
    database = 'livraria.db'
    conexao=sqlite3.connect(database)
    query = '''SELECT * from cliente'''
    try:
        cur=conexao.cursor()
        cur.execute(query)
        count = 0
        registros=cur.fetchall()
        print("Consultando todos os dados:")
        for registro in registros:
            print(registro)
            count += 1
        print("Total de Clientes:", count)
    except:
        print("Erro ao realizar a contagem, verifique os dados")
    cur.close()
    conexao.close()
if __name__ == "__main__":
    Menu()
pass