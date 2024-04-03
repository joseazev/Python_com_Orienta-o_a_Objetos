import os

def finalizar_app():
    os.system('cls')
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

def escolher_opcoes():
    opcao_escolhida = int(input(f'Escolha uma opção '))
    print(f'Você escolheu a opção {opcao_escolhida}!')

    match opcao_escolhida:
        case 1:
            print('Cadastrar Restaurantes')

        case 2:
            print('Listar Restaurantes')

        case 3:
            print('Ativar Restaurantes')

        case 4:
            finalizar_app()
        
        case _:
            print('opção inválida')

def main():
    exibir_nome_app()

    exibir_opcoes()

    escolher_opcoes()

if __name__ == '__main__':
    main()