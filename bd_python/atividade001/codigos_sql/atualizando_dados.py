import os
import sqlite3
import codigos_sql.exibindo_dados as exibir


def atualizar_dados_cliente():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()
    
    exibir.exibir_dados_cliente()
    print()
    
    id_cliente = input('Digite o id do cliente que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM cliente WHERE id = ?',(id_cliente,))
    resultado = cursor.fetchone()
    
    if not resultado:
        input("Cliente não encontrado!")
    else:
        print(f'\nNome atual: {resultado[1]}')
        print(f'Idade atual: {resultado[2]}')

        novo_nome = input(f'Novo nome ou Enter para manter "{resultado[1]}": ') or resultado[1]
        nova_idade = input(f'Nova idade ou Enter para manter "{resultado[2]}": ') or resultado[2]
        cursor.execute('UPDATE cliente SET nome = ?, idade = ? WHERE id= ?', (novo_nome, nova_idade, id_cliente))

        conec.commit()
        
        input('Dados do cliente alterados com sucesso')
        
    conec.close()
    
def atualizar_dados_destino():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)

    cursor = conec.cursor()
    
    exibir.exibir_dados_destino()
    print()
    
    id_destino = input('Digite o id do destino que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM destino WHERE id_destino = ?',(id_destino,))
    resultado = cursor.fetchone()
    
    if not resultado:
        input("Destino não encontrado!")
    else:
        print(f'\nDestino atual: {resultado[1]}')
        print(f'País atual: {resultado[2]}')

        novo_destino = input(f'Novo destino ou Enter para manter "{resultado[1]}": ') or resultado[1]
        novo_pais = input(f'Novo país ou Enter para manter "{resultado[2]}": ') or resultado[2]
        cursor.execute('UPDATE destino SET nome_destino = ?, pais = ? WHERE id_destino = ?', (novo_destino, novo_pais, id_destino))

        conec.commit()
        
        input('Dados do destino alterados com sucesso')
        
    conec.close()
    
def atualizar_empresa_aerea():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    exibir.exibir_dados_empresa_aerea()
    print()
    
    id_empresa_aerea = input('Digite o id da empresa aérea que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM empresa_aerea WHERE id_empresa_aerea = ?',(id_empresa_aerea,))
    resultado = cursor.fetchone()
    
    if not resultado:
            input("Empresa aérea não encontrada!")
    else:
        print(f'\nNome atual da empresa: {resultado[1]}')
        
        novo_nome_empresa = input(f'Novo nome da Empresa aérea ou Enter para manter "{resultado[1]}": ') or resultado[1]
        cursor.execute('UPDATE empresa_aerea SET nome_empresa_aerea = ? WHERE id_empresa_aerea= ?', (novo_nome_empresa, id_empresa_aerea))
    
        conec.commit() # Salva as transações no banco de dados
        
        input('Dados do destino alterados com sucesso')
        
    conec.close() # Fecha o banco de dados
        
def atualizar_portao_embarque():
    
    # Obter o caminho absoluto da pasta onde está o script sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    exibir.exibir_dados_portao_embarque()
    print()
    
    id_portao = input('Digite o id do portão de embarque que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM portao_embarque WHERE id_portao_embarque = ?', (id_portao,))
    resultado = cursor.fetchone()
    
    if not resultado:
        input('Portão de embarque não encontrado!')
    else:
        print(f'\nNome do portão de embarque: {resultado[1]}')
        
        novo_portao_embarque = input(f'Novo portão de embarque ou Enter para manter "{resultado[1]}": ') or resultado[1]
        cursor.execute('UPDATE portao_embarque SET nome_portao_embarque = ? WHERE id_portao_embarque = ?', (novo_portao_embarque, id_portao))
        
        conec.commit()
        
    conec.close()

def atualizar_tipo_viagem():
    
    # Criar conexão com o banco de dados
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    exibir.exibir_dados_tipo_viagem()
    print()
    
    id_tipo_viagem = input('Digite o id do tipo de viagem que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM tipo_viagem WHERE id_tipo_viagem = ?', (id_tipo_viagem,))
    resultado = cursor.fetchone()
    
    if not resultado:
        input('Tipo de viagem não encontrado!')
    else:
        print(f'\nNome do tipo de viagem: {resultado[1]}')
        
        novo_tipo_viagem = input(f'Novo tipo de viagem ou Enter para manter "{resultado[1]}": ') or resultado[1]
        cursor.execute('UPDATE tipo_viagem SET tipo_viagem = ? WHERE id_tipo_viagem = ?', (novo_tipo_viagem, id_tipo_viagem))
        
        conec.commit()
        
    conec.close()
    
def atualizar_dados_escala():
    
    # Criar conexão com o banco de dados
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho do banco de dados relativo à pasta do script
    db_path = os.path.join(base_dir, "passagens.db")

    # Conectar ao banco de dados
    conec = sqlite3.connect(db_path)
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    exibir.exibir_dados_escala()
    print()
    
    id_escala = input('Digite o id da escala que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM escala WHERE id_escala = ?', (id_escala,))
    resultado = cursor.fetchone()
    
    if not resultado:
        input('Escala não encontrada!')
    else:
        print(f'\nQuantidade de escalas: {resultado[1]}')
        
        nova_escala = input(f'QUantidade de escalas ou Enter para manter "{resultado[1]}": ') or resultado[1]
        cursor.execute('UPDATE escala SET quantidade_escala = ? WHERE id_escala = ?', (nova_escala, id_escala))
        
        conec.commit()
        
    conec.close()