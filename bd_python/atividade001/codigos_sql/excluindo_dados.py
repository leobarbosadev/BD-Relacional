# import os
import os
import sqlite3
import codigos_sql.exibindo_dados as exibir


def excluir_dados_cliente():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_cliente()
    print()

    id_cliente = input('Digite o id do cliente que deseja excluir: ')

    cursor.execute('DELETE FROM cliente WHERE id = ?',(id_cliente,))

    conec.commit()

    input('Dados do cliente excluido com sucesso')

    conec.close()

def excluir_dados_local():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_local()
    print()

    id_local = input('Digite o id do local que deseja excluir: ')

    cursor.execute('DELETE FROM local WHERE local = ?',(id_local,))

    conec.commit()

    input('Dados do local excluido com sucesso')

    conec.close()

def excluir_dados_voo():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_voo()
    print()

    id_voo = input('Digite o id do voo que deseja excluir: ')

    cursor.execute('DELETE FROM voo WHERE id_voo = ?',(id_voo,))

    conec.commit()

    input('Dados do voo excluido com sucesso')

    conec.close()

def excluir_dados_empresa_aerea():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_empresa_aerea()
    print()

    id_empresa_aerea = input('Digite o id da empresa aérea que deseja excluir: ')

    cursor.execute('DELETE FROM empresa_aerea WHERE id_empresa_aerea = ?',(id_empresa_aerea,))

    conec.commit()

    input('Dados da empresa aerea excluido com sucesso')

    conec.close()
    
def excluir_dados_portao_embarque():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_portao_embarque()
    print()

    id_portao_embarque = input('Digite o id da empresa aérea que deseja excluir: ')

    cursor.execute('DELETE FROM portao_embarque WHERE id_portao_embarque = ?',(id_portao_embarque,))

    conec.commit()

    input('Dados do portão de embarque excluido com sucesso')

    conec.close()
    
def excluir_dados_tipo_viagem():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_tipo_viagem()
    print()

    id_tipo_viagem = input('Digite o id do tipo de viagem que deseja excluir: ')

    cursor.execute('DELETE FROM tipo_viagem WHERE id_tipo_viagem = ?',(id_tipo_viagem,))

    conec.commit()

    input('Dados do tipo de viagem excluido com sucesso')

    conec.close()
    
def excluir_dados_escala():
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_escala()
    print()

    id_escala = input('Digite o id da escala que deseja excluir: ')

    cursor.execute('DELETE FROM escala WHERE id_escala = ?',(id_escala,))

    conec.commit()

    input('Dados da escala excluido com sucesso')

    conec.close()

def excluir_dados_passagem():
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir.exibir_dados_passagem()
    print()

    id_passagem = input('Digite o id da passagem que deseja excluir: ')

    cursor.execute('DELETE FROM passagem WHERE id_passagem = ?',(id_passagem,))

    conec.commit()

    input('Dados da passagem excluido com sucesso')

    conec.close()