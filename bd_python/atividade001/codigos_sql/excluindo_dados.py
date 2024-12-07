# import os
import os
import sqlite3
from codigos_sql.exibindo_dados import exibir_dados_cliente

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




