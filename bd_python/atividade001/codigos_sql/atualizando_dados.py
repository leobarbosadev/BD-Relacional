import os
import sqlite3

def atualizar_dados_cliente():
    
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    cursor = conec.cursor()
    
    os.system('cls')
    nome_cliente = input('Digite o nome do cliente que deseja atualizar: ')
    novo_nome = input('Digite o novo nome: ')
    nova_idade = input('Digite a nova idade: ')
    
    cursor.execute('UPDATE cliente SET nome = ?, idade = ? WHERE nome = ?', (novo_nome, nova_idade, nome_cliente))
    
    conec.commit()
    
    conec.close()
    
def atualizar_dados_destino():
    
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    cursor = conec.cursor()
    
    os.system('cls')
    nome_destino = input('Digite o nome do destino que deseja atualizar: ')
    novo_destino = input('Digite o novo destino: ')
    novo_pais = input('Digite o novo país: ')
    
    cursor.execute('UPDATE destino SET nome_destino = ?, pais = ?'(novo_destino, novo_pais, nome_destino))
    
    conec.commit()
    
    conec.close()
    
def atualizar_empresa_aerea():
    
    # Criar conexão com o banco de dados
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    os.system('cls')
    nome_empresa = input('Digite o nome da empresa aérea que deseja atualizar: ')
    novo_nome_empresa = input('Digite o novo nome da empresa aérea: ')
    
    cursor.execute('UPDATE empresa_aerea SET nome_empresa_aerea = ? WHERE nome_empresa_aerea = ?', (novo_nome_empresa, nome_empresa))
    
    conec.commit() # Salva as transações no banco de dados
    
    conec.close() # Fecha o banco de dados