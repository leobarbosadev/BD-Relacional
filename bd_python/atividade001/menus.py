import os
from codigos_sql.criar_tabelas_e_banco import criar_banco
from codigos_sql.inserindo_dados import inserir_dados_cliente, inserir_dados_destino, inserir_dados_empresa_aerea, inserir_dados_portao_embarque, inserir_dados_tipo_viagem, inserir_dados_escala, inserir_dados_passagem
from codigos_sql.atualizando_dados import atualizar_dados_cliente, atualizar_dados_destino, atualizar_empresa_aerea
from codigos_sql.exibindo_dados import exibir_dados_cliente, exibir_dados_destino, exibir_dados_empresa_aerea, exibir_dados_portao_embarque, exibir_dados_tipo_viagem
from codigos_sql.excluindo_dados import excluir_dados_cliente

criar_banco()


def menu_principal():
    while True:
        os.system('cls')
        print('Escolha uma opção')
        menu = input('1 - Adicionar\n'
                     + f'2 - Atualizar\n'
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
    print()
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
        menu_principal()
    elif submenu == '1':
        print()
        inserir_dados_cliente()
        input('Dados do cliente inseridos com sucesso')
        os.system('cls')
    elif submenu == '2':
        print()
        inserir_dados_destino()
        input('Dados do destino inseridos com sucesso')
        os.system('cls')
    elif submenu == '3':
        print()
        inserir_dados_empresa_aerea()
        input('Dados da empresa aérea inseridos com sucesso')
        os.system('cls')
    elif submenu == '4':
        print()
        inserir_dados_portao_embarque()
        input('Dados do portão de embarque inseridos com sucesso')
        os.system('cls')
    elif submenu == '5':
        print()
        inserir_dados_tipo_viagem()
        input('Dados do tipo de viagem inseridos com sucesso')
        os.system('cls')
    elif submenu == '6':
        print()
        inserir_dados_escala()
        input('Dados de escala inseridos com sucesso')
        os.system('cls')
    elif submenu == '7':
        print()
        inserir_dados_passagem()
        input('Dados de passgem inseridos com sucesso')
        os.system('cls')
    else:
        input('Opção invalida')
        os.system('cls')
        submenu_inserir()


def submenu_alterar():
    print()
    print('O que deseja atualizar?')
    submenu = input('1 - Cliente\n'
                    + f'2 - Destino\n'
                    + f'3 - Empresa aérea\n'
                    + f'4 - Portão de embarque\n'
                    + f'5 - Tipo de de viagem\n'
                    + f'6 - Quantidade de escalas\n'
                    + f'7 - Passagens\n'
                    + f'8 - Voltar\n\n').strip()
    if submenu == '8':
        menu_principal()
    elif submenu == '1':
        print()
        atualizar_dados_cliente()
        # input('Dados do cliente atualizados com sucesso')
        os.system('cls')
    elif submenu == '2':
        print()
        atualizar_dados_destino()
        # input('Dados do destino atualizados com sucesso')
        os.system('cls')
    elif submenu == '3':
        print()
        atualizar_empresa_aerea()
        # input('Dados da empresa aérea atualizados com sucesso')

def submenu_exibir():
    print()
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
        menu_principal()
    elif submenu == '1':
        os.system('cls')
        exibir_dados_cliente()
        print()
        input('Precione Enter para voltar')
    elif submenu == '2':
        os.system('cls')
        exibir_dados_destino()
        print()
        input('Precione Enter para voltar')
    elif submenu == '3':
        os.system('cls')
        exibir_dados_empresa_aerea()
        print()
        input('Precione Enter para voltar')
    elif submenu == '4':
        os.system('cls')
        exibir_dados_portao_embarque()
        print()
        input('Precione Enter para voltar')
    elif submenu == '5':
        os.system('cls')
        exibir_dados_tipo_viagem()
        print()
        input('Precione Enter para voltar')
        
def submenu_excluir():
    print()
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
        menu_principal()
    elif submenu == '1':
        os.system('cls')
        excluir_dados_cliente()
        print()
        input('Precione Enter para voltar')
    elif submenu == '2':
        os.system('cls')
        
        print()
        input('Precione Enter para voltar')
    elif submenu == '3':
        os.system('cls')
        ()
        print()
        input('Precione Enter para voltar')
    elif submenu == '4':
        os.system('cls')
        ()
        print()
        input('Precione Enter para voltar')
    elif submenu == '5':
        os.system('cls')
        ()
        print()
        input('Precione Enter para voltar')