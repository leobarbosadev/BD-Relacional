import os
import sqlite3

def inserir_dados_cliente():
    
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()

        os.system('cls')
        nome = input('Digite um nome: ')
        idade = int(input('Digite a idade: '))

        cursor.execute('INSERT INTO cliente (nome, idade) VALUES (?, ?)', (nome, idade))

        conec.commit()
        
        conec.close()
        
def inserir_dados_destino():
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()

        os.system('cls')
        nome_destino = input('Digite o destino: ')
        pais = input('Digite o país: ')

        cursor.execute('INSERT INTO destino (nome_destino, pais) VALUES (?, ?)', (nome_destino, pais))

        conec.commit()
        
        conec.close()

def inserir_dados_empresa_aerea():
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()

        os.system('cls')
        nome_empresa = input('Digite o nome da empresa aérea: ')

        cursor.execute('INSERT INTO empresa_aerea (nome_empresa_aerea) VALUES (?)', (nome_empresa,))

        conec.commit()
        
        conec.close()
        
def inserir_dados_portao_embarque():
        
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()

        os.system('cls')
        nome_portao_embarque = input('Digite o portão de embarque: ')

        cursor.execute('INSERT INTO portao_embarque (nome_portao_embarque) VALUES (?)', (nome_portao_embarque,))

        conec.commit()
        
        conec.close()
        
def inserir_dados_tipo_viagem():
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()

        os.system('cls')
        tipo_viagem = input('Digite o tipo de viagem: ')

        cursor.execute('INSERT INTO tipo_viagem (tipo_viagem) VALUES (?)', (tipo_viagem,))

        conec.commit()
        
        conec.close()
        
def inserir_dados_escala():
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')


        cursor = conec.cursor()

        os.system('cls')
        qtd_escala = input('Digite a quantidade de escalas ou se o voo é direto: ')

        cursor.execute('INSERT INTO escala (quantidade_escala) VALUES (?)', (qtd_escala,))

        conec.commit()
        
        conec.close()