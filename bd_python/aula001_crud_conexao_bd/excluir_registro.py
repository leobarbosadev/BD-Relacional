import os
import sqlite3

con = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python\meu_banco.db')

cursor = con.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente para excluir: ')

# Executa a exclusão com base no nome fornecido pelo usuário
cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome_cliente,))
con.commit()

print('Cliente deletado com sucesso!')

# Fecha a conexão
con.close()