import os

# apresentação 

def apresentacao():
    print("""
          
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_menu():

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o  Processo')


def escolher_opcoes():

    opcao_escolhida = int(input('Escolha uma opção: '))


    if opcao_escolhida == 1:
        print('Cadastrar restaurante')

    if opcao_escolhida == 2:
        print('Listar restaurante')

    if opcao_escolhida == 3:
        print('Ativar restaurante')

    if opcao_escolhida == 4:
        finalizar_app()

def main():

    apresentacao()

    exibir_menu()

    escolher_opcoes()

if __name__ == '__main__':
    main()