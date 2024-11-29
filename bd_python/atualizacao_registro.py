import os
import sqlite3

con = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python\meu_banco.db')

cursor = con.cursor()

os.system('cls')
nome_cliente = input('Digite o nome do cliente: ')
nova_idade = int(input('Digite a nova idade: '))

# Atualiza a idade com base no nome fornecido pelo usuário
cursor.execute('UPDATE clientes SET idade = ? WHERE nome = ?', (nova_idade, nome_cliente))

# Salva as alterações no banco de dados
con.commit()
print('Dados atualizados com sucesso!')
con.close()