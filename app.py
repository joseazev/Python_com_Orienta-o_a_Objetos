import os

restaurantes = ['Caipira','Três Marias','Xian Rio']

def limpar_tela(subtitulo):
    os.system('cls')
    print(subtitulo)


def finalizar_app():
    limpar_tela()
    print('Finalizando App\n')

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

def opcao_invalida():
    print('opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input(f'\nTecle ENTER para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    limpar_tela('Cadastrar Restaurantes')
    novo_retaurante = input('informe nome do restaurante que deseja cadastrar:\n')
    restaurantes.append(novo_retaurante)
    limpar_tela()
    print(f'\nRestaurante {restaurantes[-1]} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_retaurantes():
    limpar_tela('Listando Restaurantes\n')

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

def main():
    limpar_tela()

    exibir_nome_app()   

    exibir_opcoes()

    escolher_opcoes()

if __name__ == '__main__':
    main()