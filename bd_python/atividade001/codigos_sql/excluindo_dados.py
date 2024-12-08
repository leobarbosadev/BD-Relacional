# import os
import os
import sqlite3
from codigos_sql.exibindo_dados import exibir_dados_cliente, exibir_dados_destino, exibir_dados_empresa_aerea, exibir_dados_portao_embarque, exibir_dados_tipo_viagem, exibir_dados_escala, exibir_dados_passagem

def excluir_dados_cliente():

    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir_dados_cliente()
    print()

    id_cliente = input('Digite o id do cliente que deseja atualizar: ')

    cursor.execute('DELETE FROM cliente WHERE id = ?',(id_cliente,))

    conec.commit()

    input('Dados do cliente excluido com sucesso')

    conec.close()

def excluir_dados_destino():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir_dados_destino()
    print()

    id_destino = input('Digite o id do destino que deseja excluir: ')

    cursor.execute('DELETE FROM destino WHERE id_destino = ?',(id_destino,))

    conec.commit()

    input('Dados do destino excluido com sucesso')

    conec.close()

def excluir_dados_empresa_aerea():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()

    exibir_dados_empresa_aerea()
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

    exibir_dados_portao_embarque()
    print()

    id_portao_embarque = input('Digite o id da empresa aérea que deseja excluir: ')

    cursor.execute('DELETE FROM portao_embarque WHERE id_portao_embarque = ?',(id_portao_embarque,))

    conec.commit()

    input('Dados do portão de embarque excluido com sucesso')

    conec.close()