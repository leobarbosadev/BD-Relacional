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
    
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS portao_embarque(
        id_prtao_embarque INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_portao_embarque TEXT NOT NULL
        )
    '''
    )
    
    cursor.execute( # EXECUTIVA/ PRIMEIRA CLASSE/ ECONÔMICA
    '''
    CREATE TABLE IF NOT EXISTS tipo_viagem(
        id_tipo_viagem INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_viagem TEXT NOT NULL
        )          
    '''
    )
    
    cursor.execute( # DIRETO/ 1 ESCALA/ 2 ESCALAS/ 3 ESCALAS/ 4 ESCALAS
    '''
    CREATE TABLE IF NOT EXISTS escala(
        id_escala INTEGER PRIMARY KEY AUTOINCREMENT,
        quantidade_escala TEXT NOT NULL
        )          
    '''
    )
    
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS passagem(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_voo INTEGER NOT NULL,
        id_origem INTEGER NOT NULL,
        id_destino INTEGER NOT NULL,
        data_hora_ida TEXT NOT NULL,
        data_hora_volta TEXT NOT NULL,
        id_empresa_aerea INTEGER NOT NULL,
        id_portao_embarque INTEGER NOT NULL,
        id_tipo_viagem INTEGER NOT NULL,
        id_escala INTEGER NOT NULL
        )          
    '''
    )
     
     
     
     
