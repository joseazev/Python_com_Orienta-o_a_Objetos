import os

restaurantes = ['Caipira','Três Marias','Xian Rio']

def exibir_nome_app():

    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print(f'1. Cadasrtrar Restaurante')
    print(f'2. Listar Restaurante')
    print(f'3. Ativar Restaurante')
    print(f'4. Sair\n')

def limpar_tela(mensagem):
    os.system('cls')
    print(mensagem)

def opcao_invalida():
    print('opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input(f'\nTecle ENTER para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    limpar_tela('Cadastrar Novo Restaurante')
    novo_retaurante = input('informe nome do restaurante que deseja cadastrar:\n')
    restaurantes.append(novo_retaurante)
    print(f'\nRestaurante {restaurantes[-1]} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_retaurantes():
    limpar_tela('Listando Restaurantes\n')
    print()

    for restaurante in restaurantes:
        print(f'.{ restaurante}')

    voltar_ao_menu_principal()

def escolher_opcoes():
    opcao_escolhida = int(input(f'Escolha uma opção '))
    print(f'Você escolheu a opção {opcao_escolhida}!')

    try:
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()

            case 2:
                listar_retaurantes()

            case 3:
                print('Ativar Restaurantes')

            case 4:
                finalizar_app()
            
            case _:
                opcao_invalida()
    
    except:
        opcao_invalida()


def finalizar_app():
    limpar_tela('Finalizando App\n')
    print()

def main():
    limpar_tela('')

    exibir_nome_app()   

    exibir_opcoes()

    escolher_opcoes()

if __name__ == '__main__':
    main()