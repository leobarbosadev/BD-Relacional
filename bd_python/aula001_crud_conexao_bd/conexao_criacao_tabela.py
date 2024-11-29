import sqlite3

# conn: é a variável para conexão com o banco de dados
conn = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python\meu_banco.db')

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
    '''
)