import os
import sqlite3
from prettytable import PrettyTable

def exibir_dados_cliente():

    conec = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM cliente')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()
