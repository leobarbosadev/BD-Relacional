import sqlite3



conec = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    # Cursor permite que eu utilize comandos SQL
cursor = conec.cursor()
    
cursor.execute('SELECT * FROM cliente')
resultados = cursor.fetchall() # fetchall pega todos os dados da tabela

for row in resultados:
    print(row)