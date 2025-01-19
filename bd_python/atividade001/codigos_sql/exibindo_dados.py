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
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

    os.system('cls')

    tabela = PrettyTable()

    colunas = [descricao[0]for descricao in cursor.description]

    tabela.field_names = colunas

    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    conec.close()


def exibir_dados_local():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    cursor.execute('SELECT * FROM local')
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

    os.system('cls')

    tabela = PrettyTable()

    colunas = [descricao[0]for descricao in cursor.description]

    tabela.field_names = colunas

    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    conec.close()


def exibir_dados_voo():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    cursor.execute('SELECT * FROM voo')
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

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
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

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
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

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
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

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
    resultados = cursor.fetchall()  # fetchall pega todos os dados da tabela

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

    cursor.execute('''
        SELECT id_passagem AS Id, nome, nome_empresa_aerea AS Empresa_Aerea, origem.nome_local AS Origem, destino.nome_local AS Destino, nome_portao_Embarque AS Portao_embarque, passagem.data_ida AS Data_Ida, passagem.data_volta AS Data_Volta, tipo_viagem.tipo_viagem AS Tipo_Viagem, quantidade_escala AS Escalas
        FROM cliente 
        JOIN escala ON passagem.id_escala = escala.id_escala
        JOIN passagem ON passagem.id_cliente = cliente.id_cliente
        JOIN tipo_viagem ON passagem.id_tipo_viagem = tipo_viagem.id_tipo_viagem
        JOIN empresa_aerea ON passagem.id_empresa_aerea = empresa_aerea.id_empresa_aerea
        JOIN portao_embarque ON passagem.id_portao_embarque = portao_embarque.id_prtao_embarque
        JOIN local AS origem ON passagem.id_origem = origem.id_local
        JOIN local AS destino ON passagem.id_destino = destino.id_local;''')
    
    resultados = cursor.fetchall() # fetchall pega todos os dados da tabela
    
    os.system('cls')
    
    tabela = PrettyTable()
    
    colunas = [descricao[0]for descricao in cursor.description]
    
    tabela.field_names = colunas
    
    for row in resultados:
        tabela.add_row(row)
        
    print(tabela)
    conec.close()