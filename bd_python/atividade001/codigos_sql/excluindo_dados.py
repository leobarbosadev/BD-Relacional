import os
import sqlite3
from codigos_sql.exibindo_dados import exibir_dados_cliente

def excluir_dados_cliente():

        conec = sqlite3.connect('C:/repositorios\BD-Relacional/bd_python/atividade001\codigos_sql\passagens.db')

        cursor = conec.cursor()
        
        exibir_dados_cliente()
        print()
        
        id_cliente = input('Digite o id do cliente que deseja atualizar: ')
    
        cursor.execute('DELETE FROM cliente WHERE id = ?',(id_cliente,))
        
        conec.commit()
        
        input('Dados do cliente excluido com sucesso')
        
        conec.close()

