import os
import sqlite3
from codigos_sql.exibindo_dados import exibir_dados_cliente

def atualizar_dados_cliente():
    
    conec = sqlite3.connect('..\\BD-Relacional\\bd_python\\atividade001\\codigos_sql\\passagens.db')

    cursor = conec.cursor()
    
    exibir_dados_cliente()
    print()
    id_cliente = input('Digite o id do cliente que deseja atualizar: ')
    
    cursor.execute('SELECT * FROM cliente WHERE id = ?',(id_cliente,))
    resultado = cursor.fetchone()
    
    # print(f'Nome: {resultado[1]}')
    # print(f'Idade: {resultado[2]}')
    
    
    # novo_nome = input(f'Digite o novo nome (ou pressione Enter para manter "{resultado[1]}"): ') or resultado[1]
    # nova_idade = input(f'Digite a nova idade (ou pressione Enter para manter "{resultado[2]}"): ') or resultado[2]
    
    if not resultado:
        print("Cliente não encontrado!")
    else:
        print(f'\nNome atual: {resultado[1]}')
        print(f'Idade atual: {resultado[2]}')

        novo_nome = input(f'Novo nome ou Enter para manter "{resultado[1]}": ') or resultado[1]
        nova_idade = input(f'Nova idade ou Enter para manter "{resultado[2]}": ') or resultado[2]
        cursor.execute('UPDATE cliente SET nome = ?, idade = ? WHERE id= ?', (novo_nome, nova_idade, id_cliente))

    
        conec.commit()
        input('Dados do cliente inseridos com sucesso')
        
    conec.close()
    
def atualizar_dados_destino():
    
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

    cursor = conec.cursor()
    
    os.system('cls')
    nome_destino = input('Digite o nome do destino que deseja atualizar: ')
    novo_destino = input('Digite o novo destino: ')
    novo_pais = input('Digite o novo país: ')
    
    cursor.execute('UPDATE destino SET nome_destino = ?, pais = ?',(novo_destino, novo_pais, nome_destino))
    
    conec.commit()
    
    conec.close()
    
def atualizar_empresa_aerea():
    
    # Criar conexão com o banco de dados
    conec = sqlite3.connect('C:/Users\LEO-PC\Documents\estudos\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')
    
    # Permite que utilize comandos SQL
    cursor = conec.cursor()
    
    os.system('cls')
    nome_empresa = input('Digite o nome da empresa aérea que deseja atualizar: ')
    novo_nome_empresa = input('Digite o novo nome da empresa aérea: ')
    
    cursor.execute('UPDATE empresa_aerea SET nome_empresa_aerea = ? WHERE nome_empresa_aerea = ?', (novo_nome_empresa, nome_empresa))
    
    conec.commit() # Salva as transações no banco de dados
    
    conec.close() # Fecha o banco de dados