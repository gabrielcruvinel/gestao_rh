import sqlite3
import os
from sqlite3 import Error
global conexao
global cur
conexao=sqlite3.connect('livraria.db')
cur=conexao.cursor()

# class Pessoa:
#     def __init__(self,nome,telefone,cpf):
#         self.nome = nome
#         self.telefone = telefone
#         self.cpf = cpf
#     def setName(self, nome):
#         self.nome = nome

#     def getName(self):
#         return self.nome

#     def setTelefone(self, telefone):
#         self.telefone = telefone

#     def getTelefone(self):
#         return self.telefone
    
#     def setCPF(self, cpf):
#         self.cpf = cpf
    
#     def getCPF(self):
#         return self.cpf

# class Escolha():
#     def __init__(self, escolha):
#         int(input("DIGITE A OPÇÃO DESEJADA:"))
#         self.escolha = escolha
#     def setEscolha(self, escolha):
#         self.escolha = escolha
#     def getEscolha(self):
#         return self.escolha
class Menu():
    def __init__(self):
        print("|=================LIVRARIA=================|")
        print("|[1] => FUNCIONARIO                        |")
        print("|[2] => CLIENTE                            |")
        print("|[3] => LIVRO                              |")
        print("|[0] => SAIR                               |")
        print("|==========================================|")
        Menu.opcoesMenu(self)
    def opcoesMenu(self):
        op = int(input("DIGITE A OPÇÃO DESEJADA:"))
        while op != 0:
            if op == 1:
                pass
            elif op == 2:
                Cliente()
        Menu()
        cur.close()
        conexao.close()
class Cliente():
    def __init__(self):
        print("|=================CLIENTE=================|")
        print("|[1] => CADASTRAR CLIENTE                 |")
        print("|[2] => ATUALIZAR CADASTRO DE CLIENTE     |")
        print("|[3] => EXCLUIR CLIENTE DO SISTEMA        |")
        print("|[4] => MOSTRAR TODOS OS CLIENTES         |")
        print("|[0] => SAIR                              |")
        print("|=========================================|")
        Cliente.opcoesCliente(self)
    def opcoesCliente(self):
        op = int(input("DIGITE A OPÇÃO DESEJADA:"))
        while op != 0:
            if op == 1:
                Cliente.createCliente(self)
            elif op == 2:
                Cliente.updateCliente(self)
        Menu()
    def createCliente(self):
        cur.execute('''CREATE TABLE if not exists TB_Cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome NOT NULL,telefone INTEGER,cpf text)''')
        query = '''INSERT INTO TB_Cliente(nome, telefone, cpf) VALUES(?, ? , ?)'''
        # self.cliente=Pessoa()
        # self.cliente.setName(input("DIGITE O NOME DO CLIENTE A SER CADASTRADO:"))
        # self.cliente.setTelefone(int(input("DIGITE O TELEFONE DO CLIENTE A SER CADASTRADO:")))
        # self.cliente.setCPF(input("DIGITE O CPF DO CLIENTE A SER CADASTRADO"))
        nome = input("DIGITE O NOME DO CLIENTE A SER CADASTRADO:")
        telefone = int(input("DIGITE O TELEFONE DO CLIENTE A SER CADASTRADO:"))
        cpf = input("DIGITE O CPF DO CLIENTE A SER CADASTRADO")
        cur.execute(query, (nome.upper(), telefone, cpf))
        conexao.commit()
    
    def updateCliente(self):
        print("+================= ALTERAÇÃO DE CADASTRO =================+")
        print("|1 =>         ALTERAR NOME DO CLIENTE                     |")
        print("|2 =>         ALTERAR NUMERO DO CLIENTE                   |")
        print("|3 =>         ALTERAR CPF DO CLIENTE                      |")
        print("+=========================================================+")
        escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?      "))
        if escolha == 1:
            query = "UPDATE TB_Cliente SET nome=? WHERE cpf = ?"
            cpf = input("DIGITE O CPF DO CLIENTE A SER ALTERADO:")
            nome = input("DIGITE O NOME DO CLIENTE:")
            cur.execute(query,(nome.upper(),cpf, ))
            conexao.commit()
        elif escolha == 2:
            query = "UPDATE TB_Cliente SET numero=? WHERE cpf=?"
            cpf = input("DIGITE O CPF DO CLIENTE A SER ALTERADO:")
            numero = int(input("DIGITE O NUMERO:"))
            cur.execute(query,(numero, cpf, ))
            conexao.commit()
        elif escolha == 3:
            query = "UPDATE TB_Cliente SET cpf=? where nome=?"
            nome = input("DIGITE O NOME DO CLIENTE A SER ALTERADO:")
            cpf = input("DIGITE O CPF:")
            cur.execute(query,(cpf, nome.upper(),))
        Cliente()
# def Menu():
#     print("*******Livraria*******\n")
#     print("1 => Criar banco de dados")
#     print("2 => Cadastrar Cliente")
#     print("3 => Mostrar todos os Clientes")
#     print("4 => Deletar Cliente")
#     print("5 => Alterar Cadastro de Cliente")
#     print("0 => Sair\n")
#     escolha = int(input("Digite a opção desejada:"))
#     while escolha != 0:
#         if escolha == 1:
#             createTable()
#         elif escolha == 2:
#             nome = input("Digite o nome do Cliente:")
#             telefone = int(input("Digite o telefone do Cliente:"))
#             cpf = input("Digite o cpf do Cliente")
#             insertValue(nome, telefone, cpf)
#         elif escolha == 3:
#             showAll()
#         elif escolha == 4:
#             nome = input("Digite o nome do Cliente a ser excluído:")
#             delete(nome)
#         elif escolha == 5:
#             nome = input("Digite o nome do Cliente a ser modificado:")
#             update(nome)
#         os.system('cls' if os.name == 'nt' else 'clear')
#         Menu()
# def update(nome):
#     database = 'livraria.db'
#     conexao=sqlite3.connect(database)
#     print("================= ALTERAÇÃO DE CADASTRO =================")
#     print("1 =>         ALTERAR NOME DO CLIENTE")
#     print("2 =>         ALTERAR NUMERO DO CLIENTE")
#     print("3 =>         ALTERAR CPF DO CLIENTE")
#     escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?"))
#     if escolha == 1:
#         query = "UPDATE cliente SET nome=?"
#         try:
#             cur=conexao.cursor()
#             nome = input("Digite o Nome do Cliente:")
#             cur.execute(query,(nome,))
#             conexao.commit()
#             print("Nome alterado com sucesso")
#         except:
#             print("Erro ao alterar campo")
#         cur.close()
#         conexao.close()
#     elif escolha == 2:
#         query = "UPDATE cliente SET telefone=?"
#         try:
#             cur=conexao.cursor()
#             telefone = int(input("Digite o telefone do Cliente"))
#             cur.execute(query,(telefone,))
#             conexao.commit()
#             print("Telefone alterado com sucesso")
#         except:
#             print("Erro ao alterar campo")
#         cur.close()
#         conexao.close()
#     elif escolha == 3:
#         query = "UPDATE cliente set cpf=?"
#         try:
#             cur=conexao.cursor()
#             cpf = input("Digite o cpf do Cliente")
#             cur.execute(query,(cpf,))
#         except:
#             print("Erro ao alterar campo")
#         cur.close()
#         conexao.close()
# def delete(nome):
#     database = 'livraria.db'
#     conexao=sqlite3.connect(database)
#     query = "DELETE FROM cliente WHERE nome=?"
#     try:
#         cur=conexao.cursor()
#         cur.execute(query,(nome,))
#         conexao.commit()
#         print("Cliente Deletado com Sucesso")
#         input()
#     except:
#         print("Erro ao Deletar Cliente")
#     cur.close()
#     conexao.close()
# def createTable():
#     database = 'livraria.db'
#     conexao=sqlite3.connect(database)
#     try:
#         cur=conexao.cursor()
#         cur.execute('''CREATE TABLE if not exists cliente(id INTEGER PRIMARY KEY AUTOINCREMENT,
#          nome NOT NULL, 
#          telefone INTEGER, 
#          cpf TEXT)''')
#         conexao.commit()
#         print("Tabela criada com Sucesso!")
#         input()

#     except Error as e:
#         print("Erro:")
#         print(e)
#         conexao.rollback()
#     cur.close()
#     conexao.close()
# def insertValue(nome, telefone, cpf):
#     database = 'livraria.db'
#     conexao=sqlite3.connect(database)
#     query = '''INSERT INTO cliente (nome, telefone, cpf) VALUES (?, ?, ?)'''
#     try:
#         cur=conexao.cursor()
#         cur.execute(query,(nome, telefone, cpf))
#         conexao.commit()
#         print("Cliente cadastrado com sucesso")
#     except:
#         print("Erro ao adicionar cliente")
#     cur.close()
#     conexao.close()
# def showAll():
#     database = 'livraria.db'
#     conexao=sqlite3.connect(database)
#     query = '''SELECT * from cliente'''
#     try:
#         cur=conexao.cursor()
#         cur.execute(query)
#         count = 0
#         registros=cur.fetchall()
#         print("Consultando todos os dados:")
#         for registro in registros:
#             print(registro)
#             count += 1
#         print("Total de Clientes:", count)
#     except:
#         print("Erro ao realizar a contagem, verifique os dados")
#     cur.close()
#     conexao.close()
if __name__ == "__main__":
    Menu()
pass