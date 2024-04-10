import os

restaurantes = [{'nome':'Praça','categoria':'japone','ativo': False},
                {'nome':'Tres Marias','categoria':'brasileira','ativo':True},
                {'nome':'Festa da Nona', 'categoria':'italiano','ativo':False}]

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
    print(f'3. Mudar status de Restaurante')
    print(f'4. Sair\n')

def limpar_tela(mensagem):
    os.system('cls')
    print(mensagem)
    print()

def opcao_invalida():
    print('opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input(f'\nTecle ENTER para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    limpar_tela('Cadastrar Novo Restaurante')
    
    nome_restaurante = input('informe nome do restaurante:\n')
    categoria = input('informe a categoria do restaurante:\n')
    novo_retaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(novo_retaurante)
    print(f'\nRestaurante {restaurantes[-1]['nome']} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_retaurantes():
    limpar_tela('Listando Restaurantes\n')
    print()

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'.{nome_restaurante} | {categoria_restaurante} | {status}')

    voltar_ao_menu_principal()

def mudar_status_restaurante():
    limpar_tela('Mudar status de Restaurante')
    restaurante_encontrado = False
    nome_restaurante = input('Qual restaurante deseja mudar o status?\n')
    
    for restaurante in restaurantes:
        
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            break
        
    mensagem = f'Restaurante {restaurante['nome']} e está com ativo igual a {restaurante['ativo']}' if restaurante_encontrado else f'O restaurante não encontrado'

    print(mensagem)

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
                mudar_status_restaurante()

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