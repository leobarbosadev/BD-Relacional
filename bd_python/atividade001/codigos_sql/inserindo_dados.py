import os
import sqlite3


def inserir_dados_cliente():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    os.system('cls')
    print('Inserindo dados de clientes...')
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))

    cursor.execute(
        'INSERT INTO cliente (nome, idade) VALUES (?, ?)', (nome, idade))

    conec.commit()
    
    input('Dados do cliente inseridos com sucesso')

    conec.close()

def inserir_dados_destino():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    os.system('cls')
    nome_destino = input('Digite o destino: ')
    pais = input('Digite o país: ')

    cursor.execute(
        'INSERT INTO destino (nome_destino, pais) VALUES (?, ?)', (nome_destino, pais))

    conec.commit()
    
    input('Dados do destino inseridos com sucesso')

    conec.close()

def inserir_dados_empresa_aerea():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    os.system('cls')
    nome_empresa = input('Digite o nome da empresa aérea: ')

    cursor.execute(
        'INSERT INTO empresa_aerea (nome_empresa_aerea) VALUES (?)', (nome_empresa,))

    conec.commit()

    input('Dados da empresa aérea inseridos com sucesso')
    
    conec.close()

def inserir_dados_portao_embarque():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    os.system('cls')
    nome_portao_embarque = input('Digite o portão de embarque: ')

    cursor.execute(
        'INSERT INTO portao_embarque (nome_portao_embarque) VALUES (?)', (nome_portao_embarque,))

    conec.commit()
    
    input('Dados do portão de embarque inseridos com sucesso')

    conec.close()

def inserir_dados_tipo_viagem():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()

    os.system('cls')
    tipo_viagem = input('Digite o tipo de viagem: ')

    cursor.execute(
        'INSERT INTO tipo_viagem (tipo_viagem) VALUES (?)', (tipo_viagem,))

    conec.commit()
    
    input('Dados do tipo de viagem inseridos com sucesso')

    conec.close()

def inserir_dados_escala():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    os.system('cls')
    qtd_escala = input('Digite a quantidade de escalas ou se o voo é direto: ')

    cursor.execute(
        'INSERT INTO escala (quantidade_escala) VALUES (?)', (qtd_escala,))

    conec.commit()
    
    input('Dados de escala inseridos com sucesso')

    conec.close()

def inserir_dados_passagem():

    conec = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    cursor = conec.cursor()

    os.system('cls')
    numero_voo = input('Digite o número do voo: ')
    id_origem = input('Digite o id de origem: ')
    id_destino = input('Digite o id de destino: ')
    data_hora_ida = input('Digite a data e a hora da ida: ')
    data_hora_volta = input('Digite a data e hora da volta: ')
    id_empresa_aerea = input('Digite o id da empresa aerea: ')
    id_portao_embarque = input('Digite o id do portão de embarque: ')
    id_tipo_viagem = input('Digite o id do tipo de viagem: ')
    id_escala = input('Digite o id da escala: ')
    preco_passagem = input('Digite o preco da passagem: ')

    cursor.execute('INSERT INTO passagem (numero_voo, id_origem, id_destino, data_hora_ida, data_hora_volta, id_empresa_aerea, id_portao_embarque, id_tipo_viagem, id_escala, preco_passagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (numero_voo, id_origem, id_destino, data_hora_ida, data_hora_volta, id_empresa_aerea, id_portao_embarque, id_tipo_viagem, id_escala, preco_passagem))

    conec.commit()
    
    input('Dados de passgem inseridos com sucesso')

    conec.close()
