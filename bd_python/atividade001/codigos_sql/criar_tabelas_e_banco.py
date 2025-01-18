import os
import sqlite3


def criar_banco():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS cliente(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
        )
    '''
    )
    
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS local(
        id_local INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_local TEXT NOT NULL
        )
    '''
    )
    
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS voo(
        id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_origem INTEGER NOT NULL,
        id_destino INTEGER NOT NULL,
        data_ida TEXT NOT NULL,
        data_volta TEXT,
        FOREIGN KEY (id_origem) REFERENCES local(id_local),
        FOREIGN KEY (id_destino) REFERENCES local(id_local)
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
    
    cursor.execute( # EXECUTIVA/ PRIMEIRA CLASSE/ ECONÔMICA / PREMIUM
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
        id_passagem INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_origem INTEGER NOT NULL,
        id_destino INTEGER NOT NULL,
        data_ida TEXT NOT NULL,
        data_volta TEXT NOT NULL,
        id_voo INTEGER NOT NULL,
        id_empresa_aerea INTEGER NOT NULL,
        id_portao_embarque INTEGER NOT NULL,
        id_tipo_viagem INTEGER NOT NULL,
        id_escala INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY (id_origem) REFERENCES voo(id_origem),
        FOREIGN KEY (id_destino) REFERENCES voo(id_destino),
        FOREIGN KEY (data_ida) REFERENCES voo(data_ida),
        FOREIGN KEY (data_volta) REFERENCES voo(data_volta),
        FOREIGN KEY (id_voo) REFERENCES voo(id_voo),
        FOREIGN KEY (id_empresa_aerea) REFERENCES empresa_aerea(id_empresa_aerea),
        FOREIGN KEY (id_portao_embarque) REFERENCES portao_embarque(id_portao_embarque),
        FOREIGN KEY (id_tipo_viagem) REFERENCES tipo_viagem(id_tipo_viagem),
        FOREIGN KEY (id_escala) REFERENCES escala(id_escala)
        )
    '''
    )