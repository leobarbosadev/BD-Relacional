import os
from codigos_sql.criar_tabelas_e_banco import criar_banco
import codigos_sql.inserindo_dados as inserir
import codigos_sql.atualizando_dados as atualizar
import codigos_sql.exibindo_dados as exibir
import codigos_sql.excluindo_dados as excluir

criar_banco()

def menu_principal():
    while True:
        os.system('cls')
        print('Escolha uma opção')
        menu = input('1 - Adicionar\n'
                     + f'2 - Alterar\n'
                     + f'3 - Exibir\n'
                     + f'4 - Apagar\n'
                     + f'5 - Sair\n\n').strip()
        if menu == '5':
            input('Obrigado por utilizar nosso sistema!')
            break
        elif menu == '1':
            os.system('cls')
            submenu_inserir()
        elif menu == '2':
            os.system('cls')
            submenu_alterar()
        elif menu == '3':
            os.system('cls')
            submenu_exibir()
        elif menu == '4':
            os.system('cls')
            submenu_excluir()
        else:
            input('Opção invávida precione Enter para voltar para o menu')


def submenu_inserir():
    while True:
        print('O que deseja adicionar?')
    
        submenu = input('1 - Cliente\n'
                        + f'2 - Destino\n'
                        + f'3 - Empresa aérea\n'
                        + f'4 - Portão de embarque\n'
                        + f'5 - Tipo de de viagem\n'
                        + f'6 - Quantidade de escalas\n'
                        + f'7 - Passagens\n'
                        + f'8 - Voltar\n\n').strip()
        if submenu == '8':
            break
        elif submenu == '1':
            os.system('cls')
            inserir.inserir_dados_cliente()
            print()
        elif submenu == '2':
            os.system('cls')
            inserir.inserir_dados_destino()
            print()
        elif submenu == '3':
            os.system('cls')
            inserir.inserir_dados_empresa_aerea()
            print()
        elif submenu == '4':
            os.system('cls')
            inserir.inserir_dados_portao_embarque()
            print()
        elif submenu == '5':
            os.system('cls')
            inserir.inserir_dados_tipo_viagem()
            print()
        elif submenu == '6':
            os.system('cls')
            inserir.inserir_dados_escala()
            print()
        elif submenu == '7':
            os.system('cls')
            inserir.inserir_dados_passagem()
            print()
        else:
            input('Opção invalida')
            os.system('cls')
            submenu_inserir()
            
def submenu_alterar():
    while True:
        print('O que deseja alterar?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Destino\n'
                        + f'3 - Empresa aérea\n'
                        + f'4 - Portão de embarque\n'
                        + f'5 - Tipo de de viagem\n'
                        + f'6 - Quantidade de escalas\n'
                        + f'7 - Voltar\n\n').strip()
        if submenu == '7':
            break
        elif submenu == '1':
            os.system('cls')
            atualizar.atualizar_dados_cliente()
            print()
        elif submenu == '2':
            os.system('cls')
            atualizar.atualizar_dados_destino()
            print()
        elif submenu == '3':
            print()
            atualizar.atualizar_empresa_aerea()
            os.system('cls')
        elif submenu == '4':
            os.system('cls')
            atualizar.atualizar_portao_embarque()
            print()
        elif submenu == '5':
            os.system('cls')
            atualizar.atualizar_tipo_viagem()
            print()
        elif submenu == '6':
            os.system('cls')
            atualizar.atualizar_dados_escala()
            print()

def submenu_exibir():
    while True:
        print('O que deseja exibir?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Destino\n'
                        + f'3 - Empresa aérea\n'
                        + f'4 - Portão de embarque\n'
                        + f'5 - Tipo de de viagem\n'
                        + f'6 - Quantidade de escalas\n'
                        + f'7 - Passagens\n'
                        + f'8 - Voltar\n\n').strip()
        if submenu == '8':
            break
        elif submenu == '1':
            os.system('cls')
            exibir.exibir_dados_cliente()
            print()
            input('Precione Enter para voltar')
        elif submenu == '2':
            os.system('cls')
            exibir.exibir_dados_destino()
            print()
            input('Precione Enter para voltar')
        elif submenu == '3':
            os.system('cls')
            exibir.exibir_dados_empresa_aerea()
            print()
            input('Precione Enter para voltar')
        elif submenu == '4':
            os.system('cls')
            exibir.exibir_dados_portao_embarque()
            print()
            input('Precione Enter para voltar')
        elif submenu == '5':
            os.system('cls')
            exibir.exibir_dados_tipo_viagem()
            print()
            input('Precione Enter para voltar')
        elif submenu == '6':
            os.system('cls')
            exibir.exibir_dados_escala()
            print()
            input('Precione Enter para voltar')
        elif submenu == '7':
            os.system('cls')
            exibir.exibir_dados_passagem()
            print()
            input('Precione Enter para voltar')
        
def submenu_excluir():
    while True:
        print('O que deseja apagar?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Destino\n'
                        + f'3 - Empresa aérea\n'
                        + f'4 - Portão de embarque\n'
                        + f'5 - Tipo de de viagem\n'
                        + f'6 - Quantidade de escalas\n'
                        + f'7 - Passagens\n'
                        + f'8 - Voltar\n\n').strip()
        if submenu == '8':
            break
        elif submenu == '1':
            os.system('cls')
            excluir.excluir_dados_cliente()
            print()
        elif submenu == '2':
            os.system('cls')
            excluir.excluir_dados_destino()
            print()
        elif submenu == '3':
            os.system('cls')
            excluir.excluir_dados_empresa_aerea()
            print()
        elif submenu == '4':
            os.system('cls')
            excluir.excluir_dados_portao_embarque()
            print()
        elif submenu == '5':
            os.system('cls')
            excluir.excluir_dados_tipo_viagem()
            print()
        elif submenu == '6':
            os.system('cls')
            excluir.excluir_dados_escala()
            print()
        elif submenu == '7':
            os.system('cls')
            excluir.excluir_dados_passagem()