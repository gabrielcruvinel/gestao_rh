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
        self.op = int(input("DIGITE A OPÇÃO DESEJADA:  "))
        while self.op != 0:
            if self.op == 1:
                Funcionario()
            elif self.op == 2:
                Cliente()
            elif self.op == 3:
                Livro()
            os.system('cls' if os.name == 'nt' else 'clear')
            Menu()
        cur.close()
        conexao.close()
class Livro():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("|=================LIVRO=======================|")
        print("|[1] => CADASTRAR LIVRO                       |")
        print("|[2] => ATUALIZAR INFORMAÇÕES SOBRE LIVRO     |")
        print("|[3] => EXCLUIR LIVRO DO SISTEMA              |")
        print("|[4] => ESTOQUE                               |")
        print("|[5] => VENDER LIVRO                          |")
        print("|[0] => SAIR                                  |")
        print("|=============================================|")
        Livro.opcoesLivro(self)
    
    def opcoesLivro(self):
        self.op = int(input("DIGITE A OPÇÃO DESEJADA:  "))
        while self.op != 0:
            if self.op == 1:
                cur.execute('''CREATE TABLE if not exists  TB_Livro(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT, 
                autor TEXT, 
                editora TEXT, 
                quantidade_estoque INTEGER, 
                valor FLOAT)''')
                Livro.createLivro(self)
            elif self.op == 2:
                Livro.updateLivro(self)
            elif self.op == 3:
                Livro.deleteLivro(self)
            elif self.op == 4:
                Livro.showAllLivros(self)
            Livro()
        Menu()

    def showAllLivros(self):
        query = "SELECT * FROM TB_Livro"
        query_count = "SELECT COUNT(*) FROM TB_Livro"
        query_valor_estoque = "SELECT SUM(valor) FROM TB_Livro"
        cur.execute(query)
        count = cur.execute(query_count)
        valor_estoque = cur.execute(query_valor_estoque)
        print("TOTAL DE LIVROS EM ESTOQUE:", count)
        print("VALOR DO ESTOQUE:", valor_estoque)
        input("============>APERTE [ENTER] PARA SAIR<============")

    def deleteLivro(self):
        query = "DELETE FROM TB_Livro WHERE titulo=?"
        titulo = input("DIGITE O NOME DO FUNCIONARIO A SER EXCLUIDO")
        cur.execute(query,(titulo.upper(),))
        cur.commit()
        print("LIVRO EXCLUIDO COM SUCESSO")
        input("APERTE [ENTER] PARA VOLTAR")

    def createLivro(self):
        query = ''' INSERT INTO TB_Livro(titulo, autor, editora, quantidade_estoque, valor) VALUES (?,?,?,?,?)'''
        titulo = input("DIGITE O TITULO DO LIVRO A SER CADASTRADO:")
        autor = input("DIGITE O AUTOR DO LIVRO:")
        editora = input("DIGITE A EDITORA DO LIVRO")
        quantidade_estoque = int(input("DIGITE A QUANTIDADE DE LIVROS QUE FORAM RECEBIDOS:"))
        valor = float(input("DIGITE O VALOR DO LIVRO:"))
        cur.execute(query,(titulo.upper(), autor.upper(), editora.upper(), quantidade_estoque, valor))
        conexao.commit()
        print("LIVRO CADASTRADO COM SUCESSO")
    
    def updateLivro(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("+================= ALTERAÇÃO DE CADASTRO DE LIVRO======================+")
        print("|1 =>         ALTERAR TITULO DO LIVRO                                  |")
        print("|2 =>         ALTERAR AUTOR DO LIVRO                                   |")
        print("|3 =>         ALTERAR EDITORA DO LIVRO                                 |")
        print("|4 =>         ALTERAR QUANTIDADE DO LIVRO                              |")
        print("|5 =>         ALTERAR VALOR DO LIVRO                                   |")
        print("|0 =>                   SAIR                                           |")
        print("+======================================================================+")
        self.escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?      "))
        while self.escolha !=0 :
            if self.escolha == 1:
                Livro.updateTitulo(self)
            elif self.escolha == 2:
                Livro.updateAutor(self)
            elif self.escolha == 3:
                Livro.updateEditora(self)
            elif self.escolha == 4:
                Livro.updateEditora(self)
            elif self.escolha == 5:
                Livro.updateValor(self)
            Livro.updateLivro(self)
        Menu()

    def updateValor(self):
        query = '''UPDATE TB_Livro SET valor=? where titulo=?'''
        titulo = input("DIGITE O TITULO DO LIVRO:")
        valor = float(input("DIGITE O VALOR DO LIVRO:"))
        cur.execute(query,(valor, titulo.upper()))
        conexao.commit()
        print("ESTOQUE ALTERADO COM SUCESSO")
        input("============>APERTE [ENTER] PARA SAIR<============")

    def updateQuantidade(self):
        query = '''UPDATE TB_Livro set quantidade_estoque = ? where titulo=?'''
        titulo = input("DIGITE O TITULO DO LIVRO:")
        quantidade_estoque = int(input("DIGITE A QUANTIDADE DE LIVROS EM ESTOQUE:"))
        cur.execute(query,(quantidade_estoque, titulo.upper(),))
        conexao.commit()
        print("ESTOQUE ALTERADO COM SUCESSO")
        input("============>APERTE [ENTER] PARA SAIR<============")

    def updateEditora(self):
        query = "UPDATE TB_Livro SET editora=? where titulo=?"
        titulo = input("DIGITE O TITULO DO LIVRO:")
        editora = input("DIGITE A EDITORA DO LIVRO A SER ALTERADO:")
        cur.execute(query,(editora.upper(), titulo.upper(),))
        conexao.commit()
        print("EDITORA ALTERADA COM SUCESSO")
        input("APERTE [ENTER] PARA VOLTAR AO MENU ANTERIOR")
        print("FUNCIONARIO ALTERADO COM SUCESSO")
        input("============>APERTE [ENTER] PARA SAIR<============")

    def updateTitulo(self):
        query = "UPDATE TB_Livro SET titulo=? WHERE autor = ?"
        titulo = input("DIGITE O TITULO DO LIVRO SER ALTERADO:")
        autor = input("DIGITE O AUTOR DO LIVRO:")
        cur.execute(query,(titulo.upper(),autor.upper(), ))
        conexao.commit()
        print("TITULO ALTERADO COM SUCESSO")
        input("APERTE [ENTER] PARA VOLTAR AO MENU ANTERIOR")

    def updateAutor(self):
        query = "UPDATE TB_Livro SET autor=? WHERE titulo=?"
        titulo = input("DIGITE O TITULO DO LIVRO:")        
        autor = input("DIGITE O AUTOR DO LIVRO A SER ALTERADO:")
        cur.execute(query,(autor.upper(), titulo.upper(), ))        
        conexao.commit()
        print("AUTOR ALTERADO COM SUCESSO")
        input("APERTE [ENTER] PARA VOLTAR AO MENU ANTERIOR")                
class Funcionario():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("|=================FUNCIONARIO=================|")
        print("|[1] => CADASTRAR FUNCIONARIO                 |")
        print("|[2] => ATUALIZAR CADASTRO DE FUNCIONARIO     |")
        print("|[3] => EXCLUIR FUNCIONARIO DO SISTEMA        |")
        print("|[4] => MOSTRAR TODOS OS FUNCIONARIOS         |")
        print("|[0] => SAIR                                  |")
        print("|=============================================|")
        Funcionario.opcoesFuncionario(self)
    def opcoesFuncionario(self):
        self.op = int(input("DIGITE A OPÇÃO DESEJADA:"))
        while self.op != 0:
            if self.op == 1:
                cur.execute('''CREATE TABLE if not exists TB_Funcionario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, telefone INTEGER, cpf TEXT)''')
                Funcionario.createFuncionario(self)
            elif self.op == 2:
                Funcionario.updateFuncionario(self)
            elif self.op == 3:
                Funcionario.deleteFuncionario(self)
            elif self.op == 4:
                Funcionario.showAllfuncionarios(self)
            Funcionario()
        Menu()
    def createFuncionario(self):
        query = ''' INSERT INTO TB_Funcionario(nome, telefone, cpf) VALUES(?,?,?)'''
        nome = input("DIGITE O NOME DO FUNCIONARIO A SER CADASTRADO:")
        telefone = int(input("DIGITE O TELEFONE DO FUNCIONARIO A SER CADASTRADO:"))
        cpf = input("DIGITE O CPF DO FUNCIONARIO A SER CADASTRADO:")
        cur.execute(query, (nome.upper(), telefone, cpf))
        conexao.commit()
        print("FUNCIONARIO CADASTRADO\n")

    def updateFuncionario(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("+================= ALTERAÇÃO DE CADASTRO======================+")
        print("|1 =>         ALTERAR NOME DO FUNCIONARIO                     |")
        print("|2 =>         ALTERAR NUMERO DO FUNCIONARIO                   |")
        print("|3 =>         ALTERAR CPF DO FUNCIONARIO                      |")
        print("|0 =>                   SAIR                                  |")
        print("+=============================================================+")
        self.escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?      "))
        while self.escolha !=0 :
            if self.escolha == 1:
                Funcionario.updateNomeFuncionario(self)
            elif self.escolha == 2:
                Funcionario.updateNumeroFuncionario(self)
            elif self.escolha == 3:
                Funcionario.updateCPFFuncionario(self)
            print("FUNCIONARIO ALTERADO COM SUCESSO")
            input("============>APERTE [ENTER] PARA SAIR<============")
            Funcionario.updateFuncionario(self)
        Menu()

    def updateCPFFuncionario(self):
        query = "UPDATE TB_Funcionario SET cpf=? where nome=?"
        nome = input("DIGITE O NOME DO FUNCIONARIO A SER ALTERADO:")        
        cpf = input("DIGITE O CPF:")        
        cur.execute(query,(cpf, nome.upper(),))        
        conexao.commit()        
    
    def updateNomeFuncionario(self):
        query = "UPDATE TB_Funcionario SET nome=? WHERE cpf = ?"
        cpf = input("DIGITE O CPF DO FUNCIONARIO A SER ALTERADO:")        
        nome = input("DIGITE O NOME DO CLIENTE:")        
        cur.execute(query,(nome.upper(),cpf, ))        
        conexao.commit()        
    
    def updateNumeroFuncionario(self):
        query = "UPDATE TB_Funcionario SET numero=? WHERE cpf=?"
        cpf = input("DIGITE O CPF DO FUNCIONARIO A SER ALTERADO:")        
        numero = int(input("DIGITE O NUMERO:"))        
        cur.execute(query,(numero, cpf, ))        
        conexao.commit() 

    def deleteFuncionario(self):
        query = "DELETE FROM TB_Funcionario WHERE nome=?"
        nome = input("DIGITE O NOME DO FUNCIONARIO A SER EXCLUIDO")
        cur.execute(query,(nome.upper(),))
        cur.commit()

    def showAllfuncionarios(self):
        query = '''SELECT * FROM TB_Funcionario'''
        cur.execute(query)
        count = 0
        registros = cur.fetchall()
        for registro in registros:
            print(registro)
            count += 1
        print("TOTAL DE FUNCIONARIOS CADASTRADOS:", count)
        input("============>APERTE [ENTER] PARA SAIR<============")

class Cliente():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("|=================CLIENTE=================|")
        print("|[1] => CADASTRAR CLIENTE                 |")
        print("|[2] => ATUALIZAR CADASTRO DE CLIENTE     |")
        print("|[3] => EXCLUIR CLIENTE DO SISTEMA        |")
        print("|[4] => MOSTRAR TODOS OS CLIENTES         |")
        print("|[0] => SAIR                              |")
        print("|=========================================|")
        Cliente.opcoesCliente(self)
    def opcoesCliente(self):
        self.op = int(input("DIGITE A OPÇÃO DESEJADA:  "))
        while self.op != 0:
            if self.op == 1:
                cur.execute('''CREATE TABLE if not exists TB_Cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome NOT NULL,telefone INTEGER,cpf text)''')
                Cliente.createCliente(self)
            elif self.op == 2:
                Cliente.updateCliente(self)
            elif self.op == 3:
                Cliente.deleteCliente(self)
            elif self.op == 4:
                Cliente.showAllclientes(self)
            Cliente()
        Menu()
    def createCliente(self):
        query = '''INSERT INTO TB_Cliente(nome, telefone, cpf) VALUES(?, ? , ?)'''
        # self.cliente=Pessoa()
        # self.cliente.setName(input("DIGITE O NOME DO CLIENTE A SER CADASTRADO:"))
        # self.cliente.setTelefone(int(input("DIGITE O TELEFONE DO CLIENTE A SER CADASTRADO:")))
        # self.cliente.setCPF(input("DIGITE O CPF DO CLIENTE A SER CADASTRADO"))
        nome = input("DIGITE O NOME DO CLIENTE A SER CADASTRADO:")
        telefone = int(input("DIGITE O TELEFONE DO CLIENTE A SER CADASTRADO:"))
        cpf = input("DIGITE O CPF DO CLIENTE A SER CADASTRADO:")
        cur.execute(query, (nome.upper(), telefone, cpf))
        conexao.commit()
        print("CLIENTE CADASTRADO\n")
    
    def updateCliente(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("+================= ALTERAÇÃO DE CADASTRO =================+")
        print("|1 =>         ALTERAR NOME DO CLIENTE                     |")
        print("|2 =>         ALTERAR NUMERO DO CLIENTE                   |")
        print("|3 =>         ALTERAR CPF DO CLIENTE                      |")
        print("+=========================================================+")
        self.escolha = int(input("DESEJA ALTERAR QUAL CAMPO DE CADASTRO?      "))
        if self.escolha == 1:
            Cliente.updateNomeCliente(self)
        elif self.escolha == 2:
            Cliente.updateNumeroCliente(self)
        elif self.escolha == 3:
            Cliente.updateCPFCliente(self)
        print("CLIENTE ALTERADO COM SUCESSO")
        input("============>APERTE [ENTER] PARA SAIR<============")
        Cliente()

    def updateNumeroCliente(self):
        query = "UPDATE TB_Cliente SET numero=? WHERE cpf=?"
        cpf = input("DIGITE O CPF DO CLIENTE A SER ALTERADO:")    
        numero = int(input("DIGITE O NUMERO:"))    
        cur.execute(query,(numero, cpf, ))    
        conexao.commit() 

    def updateNomeCliente(self):
        query = "UPDATE TB_Cliente SET nome=? WHERE cpf = ?"
        cpf = input("DIGITE O CPF DO CLIENTE A SER ALTERADO:")    
        nome = input("DIGITE O NOME DO CLIENTE:")    
        cur.execute(query,(nome.upper(),cpf, ))    
        conexao.commit()   

    def updateCPFCliente(self):
        query = "UPDATE TB_Cliente SET numero=? WHERE cpf=?"
        cpf = input("DIGITE O CPF DO CLIENTE A SER ALTERADO:")    
        numero = int(input("DIGITE O NUMERO:"))    
        cur.execute(query,(numero, cpf, ))    
        conexao.commit()   
        
    def deleteCliente(self):
        query = "DELETE FROM TB_Cliente WHERE nome=?"
        nome = input("DIGITE O NOME DO CLIENTE A SER EXCLUIDO:")
        cur.execute(query,(nome.upper(),))
        conexao.commit()
    
    def showAllclientes(self):
        query = '''SELECT * FROM TB_Cliente'''
        cur.execute(query)
        count = 0
        registros = cur.fetchall()
        print("CONSULTANDO TODOS OS DADOS...")
        for registro in registros:
            print(registro)
            count +=1
        print("TOTAL DE CLIENTES CADASTRADOS:", count)
        input("============>APERTE [ENTER] PARA SAIR<============")

if __name__ == "__main__":
    Menu()
pass