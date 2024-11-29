import sqlite3

# Conexão com o banco de dados
con = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python/aula001_crud_conexao_bd\meu_banco.db')

cursor = con.cursor() # O cursor deixa eu utilizar comandos SQL

dados_varios_clientes = [
    ('Maria Souza', 25),
    ('Carlos Pereira', 35),
    ('Pedro José', 28),
    ('Ana Costa', 28),
    ('Luís Gomes', 30),
    ('Fernada Lima', 22),
    ('Roberto Silva', 40),
    ('Juliana Almeida', 33),
    ('Lucas Martins', 27),
    ('Sofia Ferreira', 31),
]
cursor.executemany( # Permite exercutar várias linhas
    'INSERT INTO clientes (nome, idade) VALUES (?,?)', dados_varios_clientes)
con.commit() # Salvo minhas informações

con.close() # Fecho meu banco SEMPRE FECHAR O BANCO