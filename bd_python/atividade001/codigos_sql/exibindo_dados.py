import os
import sqlite3
from prettytable import PrettyTable


def exibir_dados_cliente():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

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
    
def exibir_dados_destino():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM destino')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()

def exibir_dados_empresa_aerea():
        
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM empresa_aerea')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()
    
def exibir_dados_portao_embarque():
        
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM portao_embarque')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()

def exibir_dados_tipo_viagem():
        
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM tipo_viagem')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()

def exibir_dados_escala():
            
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM escala')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()

def exibir_dados_passagem():
            
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    cursor.execute('SELECT * FROM passagem')
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()