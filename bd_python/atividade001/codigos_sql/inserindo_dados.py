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

def inserir_dados_local():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    os.system('cls')
    nome_local = input('Digite o local: ')

    cursor.execute(
        'INSERT INTO local (nome_local) VALUES (?)', (nome_local,))

    conec.commit()
    
    input('Dados do local inseridos com sucesso')

    conec.close()
    
def inserir_dados_voo():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    # Cursor permite que eu utilize comandos SQL
    cursor = conec.cursor()
    
    os.system('cls')
    id_origem = input('Digite o id do local de origem: ')
    id_destino = input('Digite o id do local de destino: ')
    data_ida = input('Digite a data de ida (YYYY-MM-DD): ')
    data_volta = input('Digite a data de volta (YYYY-MM-DD):')

    cursor.execute(
        'INSERT INTO voo (id_origem, id_destino, data_ida, data_volta) VALUES (?, ?, ?, ?)', (id_origem, id_destino, data_ida, data_volta))

    conec.commit()
    
    input('Dados do voo inseridos com sucesso')

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
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()
    os.system('cls')
    id_cliente = input('Digite o id do cliente: ')
    id_origem = input('Digite o id de origem: ')
    id_local = input('Digite o id de local: ')
    data_ida = input('Digite a data da ida: ')
    data_volta = input('Digite a data da volta: ')
    id_voo = input('Digite o id do voo: ')
    id_empresa_aerea = input('Digite o id da empresa aerea: ')
    id_portao_embarque = input('Digite o id do portão de embarque: ')
    id_tipo_viagem = input('Digite o id do tipo de viagem: ')
    id_escala = input('Digite o id da escala: ')

    cursor.execute('INSERT INTO passagem (id_cliente, id_origem, id_local, data_ida, data_volta, id_voo, id_empresa_aerea, id_portao_embarque, id_tipo_viagem, id_escala) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (id_cliente, id_origem, id_local, data_ida, data_volta, id_voo, id_empresa_aerea, id_portao_embarque, id_tipo_viagem, id_escala))

    conec.commit()
    
    input('Dados de passgem inseridos com sucesso')

    conec.close()
