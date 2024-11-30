# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 02/12/2024
# A atividade proposta consiste em desenvolver um sistema de gerenciamento de passagens aéreas utilizando 
# Python e o banco de dados SQLite3, aplicando o conceito de CRUD(Create, Read, Update e Delete) para manipulação dos dados. 
# O sistema deve permitir o cadastro de informações essenciais, como nome do passageiro, número do voo, destino, data e hora da viagem, 
# preço do bilhete, entre outros detalhes relevantes. Com a estrutura de CRUD, os usuários devem poder 
# adicionar novos registros de passagens, visualizar a lista de passagens cadastradas, 
# atualizar informações(por exemplo, ajustar horários ou destinos) e, quando necessário, excluir registros de passagens.

# import sqlite3
import os


while True:
    os.system('cls')
    print('Escolha uma opção')
    menu = input('1 - Adicionar\n'
                 +f'2 - Atualizar\n'
                 +f'3 - Exibir\n'
                 +f'4 - Apagar\n'
                 +f'5 - Sair\n\n').strip()
    if menu == '5':
        print('Finalizado')
        break
    elif menu == '1':
        input('Adicionado')
    elif menu == '2':
        input('Atualizado')
    elif menu == '3':
        input('Exibido')
    elif menu == '4':
        input('Apagado')