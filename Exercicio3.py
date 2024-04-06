# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

import os

def limpa_tela():
    
    os.system('cls')

usuario = 'joseazev'
senha   = '2457'

def apresentacao():
    print("""

░█████╗░░█████╗░███████╗░██████╗░██████╗░█████╗░  ░█████╗░░█████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗
███████║██║░░╚═╝█████╗░░╚█████╗░╚█████╗░██║░░██║  ███████║██║░░██║
██╔══██║██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║  ██╔══██║██║░░██║
██║░░██║╚█████╔╝███████╗██████╔╝██████╔╝╚█████╔╝  ██║░░██║╚█████╔╝
╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░╚═════╝░░╚════╝░  ╚═╝░░╚═╝░╚════╝░

░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
""")

def verrificar_identidade(usuario,usuario_escrito,senha,senha_escrita):
    if usuario_escrito == usuario:
        if senha == senha_escrita:
            return f'Bem vindo {usuario}'
        
        return f'senha incorreta'
    
    return f'Usuário não encontrado'


def main():
    
    limpa_tela()
    apresentacao()

    usuario_escrito = input('Informe o usuário: ')
    senha_escrita   = input('Informe a senha:   ')

    print(verrificar_identidade(usuario,usuario_escrito,senha,senha_escrita))

if __name__ == '__main__':
    main()

