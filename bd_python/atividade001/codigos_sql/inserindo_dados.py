import os
import sqlite3

def inserir_dados_cliente():
    
        nome = input('Digite um nome: ')
        idade = int(input('Digite a idade: '))
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()


        cursor.execute('INSERT INTO cliente (nome, idade) VALUES (?, ?)', (nome, idade))

        conec.commit()
        
        conec.close()
        
def inserir_dados_destino():
    
        nome_destino = input('Digite o destino: ')
        pais = input('Digite o país: ')
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()


        cursor.execute('INSERT INTO destino (nome_destino, pais) VALUES (?, ?)', (nome_destino, pais))

        conec.commit()
        
        conec.close()

def inserir_dados_empresa_aerea():
    
        nome_empresa = input('Digite o nome da empresa: ')
        
        # Criando conexão com o banco
        conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        # Cursor permite que eu utilize comandos SQL
        cursor = conec.cursor()


        cursor.execute('INSERT INTO empresa_aerea (nome_empresa_aerea) VALUES (?)', (nome_empresa,))

        conec.commit()
        
        conec.close()