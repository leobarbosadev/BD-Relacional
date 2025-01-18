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
        menu = input('1 - Inserir\n'
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
                        + f'2 - Local\n'
                        + f'3 - Voo\n'
                        + f'4 - Empresa aérea\n'
                        + f'5 - Portão de embarque\n'
                        + f'6 - Tipo de de viagem\n'
                        + f'7 - Quantidade de escalas\n'
                        + f'8 - Passagens\n'
                        + f'9 - Voltar\n\n').strip()
        if submenu == '9':
            break
        elif submenu == '1':
            while True:
                os.system('cls')
                inserir.inserir_dados_cliente()
                print()
                opcao = input('Deseja adicionar mais clientes? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '2':
            while True:
                os.system('cls')
                inserir.inserir_dados_local()
                print()
                opcao = input('Deseja adicionar mais locais? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '3':
            while True:
                os.system('cls')
                inserir.inserir_dados_voo()
                print()
                opcao = input('Deseja adicionar mais voos? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '4':
            while True:
                os.system('cls')
                inserir.inserir_dados_empresa_aerea()
                print()
                opcao = input('Deseja adicionar mais empresas aéreas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '5':
            while True:
                os.system('cls')
                inserir.inserir_dados_portao_embarque()
                print()
                opcao = input('Deseja adicionar mais portões de embarque? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '6':
            while True:
                os.system('cls')
                inserir.inserir_dados_tipo_viagem()
                print()
                opcao = input('Deseja adicionar mais tipos de viagem? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '7':
            while True:
                os.system('cls')
                inserir.inserir_dados_escala()
                print()
                opcao = input('Deseja adicionar mais escalas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '8':
            while True:
                os.system('cls')
                inserir.inserir_dados_passagem()
                print()
                opcao = input('Deseja adicionar mais passagens? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        else:
            input('Opção invalida')
            os.system('cls')
            submenu_inserir()
            
def submenu_alterar():
    while True:
        print('O que deseja alterar?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Local\n'
                        + f'3 - Voo\n'
                        + f'4 - Empresa Aérea\n'
                        + f'5 - Portão de embarque\n'
                        + f'6 - Tipo de de viagem\n'
                        + f'7 - Quantidade de escalas\n'
                        + f'8 - Voltar\n\n').strip()
        if submenu == '8':
            break
        elif submenu == '1':
            while True:
                os.system('cls')
                atualizar.atualizar_dados_cliente()
                print()
                opcao = input('Deseja atualizar mais clientes? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '2':
            while True:
                os.system('cls')
                atualizar.atualizar_dados_local()
                print()
                opcao = input('Deseja atualizar mais locais? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '3':
            while True:
                os.system('cls')
                atualizar.atualizar_empresa_aerea()
                print()
                opcao = input('Deseja adicionar mais empresas aéreas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '4':
            while True:
                os.system('cls')
                atualizar.atualizar_portao_embarque()
                print()
                opcao = input('Deseja adicionar mais portões de embarque? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '5':
            while True:
                os.system('cls')
                atualizar.atualizar_tipo_viagem()
                print()
                opcao = input('Deseja adicionar mais tipos de viagens? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '6':
            while True:
                os.system('cls')
                atualizar.atualizar_dados_escala()
                print()
                opcao = input('Deseja adicionar mais escalas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break

def submenu_exibir():
    while True:
        print('O que deseja exibir?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Local\n'
                        + f'3 - Voo\n'
                        + f'4 - Empresa aérea\n'
                        + f'5 - Portão de embarque\n'
                        + f'6 - Tipo de de viagem\n'
                        + f'7 - Quantidade de escalas\n'
                        + f'8 - Passagens\n'
                        + f'9 - Voltar\n\n').strip()
        if submenu == '9':
            break
        elif submenu == '1':
            exibir.exibir_dados_cliente()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '2':
            exibir.exibir_dados_local()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '3':
            exibir.exibir_dados_voo()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '4':
            exibir.exibir_dados_empresa_aerea()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '5':
            exibir.exibir_dados_portao_embarque()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '6':
            exibir.exibir_dados_tipo_viagem()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '7':
            exibir.exibir_dados_escala()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        elif submenu == '8':
            exibir.exibir_dados_passagem()
            print()
            input('Precione Enter para voltar')
            os.system('cls')
        
def submenu_excluir():
    while True:
        print('O que deseja apagar?')
        submenu = input('1 - Cliente\n'
                        + f'2 - Local\n'
                        + f'3 - Empresa aérea\n'
                        + f'4 - Portão de embarque\n'
                        + f'5 - Tipo de de viagem\n'
                        + f'6 - Quantidade de escalas\n'
                        + f'7 - Passagens\n'
                        + f'8 - Voltar\n\n').strip()
        if submenu == '8':
            break
        elif submenu == '1':
            while True:
                os.system('cls')
                excluir.excluir_dados_cliente()
                print()
                opcao = input('Deseja excluir mais clientes? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '2':
            while True:
                os.system('cls')
                excluir.excluir_dados_destin()
                print()
                opcao = input('Deseja excluir mais locais? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '3':
            while True:
                os.system('cls')
                excluir.excluir_dados_empresa_aerea()
                print()
                opcao = input('Deseja excluir mais empresas aéreas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '4':
            while True:
                os.system('cls')
                excluir.excluir_dados_portao_embarque()
                print()
                opcao = input('Deseja excluir mais portões de embarque? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '5':
            while True:
                os.system('cls')
                excluir.excluir_dados_tipo_viagem()
                print()
                opcao = input('Deseja excluir mais tipos de viagens? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '6':
            while True:
                os.system('cls')
                excluir.excluir_dados_escala()
                print()
                opcao = input('Deseja excluir mais escalas? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break
        elif submenu == '7':
            while True:
                os.system('cls')
                excluir.excluir_dados_passagem()
                print()
                opcao = input('Deseja excluir mais passagens? (S-Sim)').lower()
                if opcao != 's':
                    os.system('cls')
                    break