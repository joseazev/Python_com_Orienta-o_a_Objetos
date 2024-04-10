# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

import os
def limpa_tela():
    os.system('cls')

def apresentacao():
    print('''

    ████████╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░
    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░░░██║░░░███████║██████╦╝██║░░██║███████║██║░░██║███████║
    ░░░██║░░░██╔══██║██╔══██╗██║░░██║██╔══██║██║░░██║██╔══██║
    ░░░██║░░░██║░░██║██████╦╝╚█████╔╝██║░░██║██████╔╝██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
    ''')

def taboada():
    try:
        numero = int(input('Qual taboada de hoje? '))
        print()
        for i in range(1,11):
            print(f'{i:2} x {numero} = {i*numero:3}')
        
    except:
        print(f'Não foi possível criar taboada com esse numero')

        input(f'\nTecle ENTER para voltar ao menu principal')
        main()

def main():
    limpa_tela()

    apresentacao()

    taboada()

if __name__ == '__main__':
    main()