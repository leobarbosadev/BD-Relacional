import os
import sqlite3
from prettytable import PrettyTable

con = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python\meu_banco.db')

cursor = con.cursor()

cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall() # fetchall pega todos os dados da tabela

os.system('cls')
for row in resultados:
    print(row)

print('')
print('-' * 50,'\nSAÍDA FORMATADA COM PRETTYTABLE\n')

#Cria a tabela PrettyTable e define os nomes das colunas
tabela = PrettyTable() # Crio um objeto da classe PrettyTable()
# Obtém os nomes das colunas a partir de cursor.description
colunas = [descricao[0] for descricao in cursor.description]
# Define os nomes das colunas na tabela PrettyTable
tabela.field_names = colunas

# Adiciona as linhas à tabela
for row in resultados:
    tabela.add_row(row)

print(tabela)
con.close()