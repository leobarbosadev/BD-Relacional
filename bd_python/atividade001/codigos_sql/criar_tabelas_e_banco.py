import sqlite3
def criar_banco():

    # Criando conexão com o banco
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS cliente(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
        )
    '''
    )
    
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS destino(
        id_destino INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_destino TEXT NOT NULL,
        pais TEXT
        )
    '''
    )
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS empresa_aerea(
        id_empresa_aerea INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_empresa_aerea TEXT NOT NULL
        )
        '''
    )
     
