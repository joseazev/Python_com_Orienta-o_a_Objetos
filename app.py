import os

restaurantes = [{'nome':'Praça','categoria':'japone','ativo': False},
                {'nome':'Tres Marias','categoria':'brasileira','ativo':True},
                {'nome':'Festa da Nona', 'categoria':'italiano','ativo':False}]

def exibir_nome_app():
    '''Função cria um cabeçalho amigável
    
        outputs:
        cabeçalho do app de maneira amigável.
    '''

    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''Apresenta o menu para escolha do usuário

    outputs:
       Menu na tela para visualização do usuário
    '''
    print(f'1. Cadasrtrar Restaurante')
    print(f'2. Listar Restaurante')
    print(f'3. Mudar status de Restaurante')
    print(f'4. Sair\n')

def limpar_tela(mensagem):
    """limpa a tela de itens anteriores esctitos e apresenta uma mensagem recebida de outra fução.

    atributo:
       recebe mensagem pre definida de outras funções.

    outputs:
       subtitulo amigável
    """
    os.system('cls')
    tamanho = len(mensagem)+4
    linha = '*' * (tamanho)
    print(linha)
    print(f'{mensagem.center(tamanho)}')
    print(linha)
    print()

def opcao_invalida():
    '''Apresenta mensagem quando houver algum problema de inserção inválida
    '''
    print('opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Função que volta para a função principal

    input: Pressionar a tecla ENTER
    '''
    input(f'\nTecle ENTER para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes
    
        Inputs:
        - Nome do Restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
    '''

    limpar_tela('Cadastrar Novo Restaurante')
    nome_restaurante = input('informe nome do restaurante:\n')
    categoria = input('informe a categoria do restaurante:\n')
    novo_retaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(novo_retaurante)
    print(f'\nRestaurante {restaurantes[-1]['nome']} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_retaurantes():
    """
    Lista os restaurantes disponíveis na tela, mostrando o nome, categoria e status.

    A função limpa a tela, imprime um cabeçalho formatado e, em seguida,
    itera sobre a lista de restaurantes fornecida. Para cada restaurante,
    imprime o nome, categoria e status (Ativado ou Desativado) formatados em colunas.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    """
    limpar_tela('Listando Restaurantes\n')
    print()

    print(f'{'Restaurante'.center(21)}|{'Categoria'.center(21)}|{'Status'.center(12)}')
    print("-"*60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' {nome_restaurante.ljust(20)}| {categoria_restaurante.ljust(20)}| {status}')

    voltar_ao_menu_principal()

def mudar_status_restaurante():
    """
    Altera o status de um restaurante (Ativado ou Desativado) com base no nome fornecido pelo usuário.

    Esta função solicita ao usuário o nome do restaurante que ele deseja alterar o status.
    Em seguida, verifica se o restaurante existe na lista de restaurantes.
    Se encontrado, inverte o status do restaurante entre Ativado e Desativado e informa ao usuário.
    Se não encontrado, informa ao usuário que o restaurante não foi encontrado.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    """

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
    """
    Permite ao usuário escolher uma opção de um menu e executa a ação correspondente.

    Esta função solicita ao usuário que escolha uma opção do menu digitando um número.
    Em seguida, utiliza uma expressão de correspondência (match) para determinar qual ação deve ser executada
    com base na opção escolhida.
    As opções válidas são:
        1. Cadastrar um novo restaurante
        2. Listar os restaurantes
        3. Mudar o status de um restaurante
        4. Finalizar o aplicativo
    Se uma opção inválida for escolhida, a função chama a função opcao_invalida().

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    """
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
    """
    Finaliza o aplicativo, exibindo uma mensagem de encerramento.

    Esta função limpa a tela e imprime uma mensagem indicando que o aplicativo está sendo finalizado.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    """
    limpar_tela('Finalizando App\n')
    print()

def main():
    """
    Função principal que executa o aplicativo.

    Esta função é responsável por iniciar o aplicativo.
    Limpa a tela, exibe o nome do aplicativo, exibe as opções disponíveis e permite ao usuário escolher uma opção.

    Parâmetros:
    Nenhum.

    Retorno:
    Nenhum.
    """
    os.system('cls')

    exibir_nome_app()   

    exibir_opcoes()

    escolher_opcoes()

if __name__ == '__main__':
    main()