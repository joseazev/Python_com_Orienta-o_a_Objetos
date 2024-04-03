# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

import os

def limpa_tela():
    
    os.system('cls')

limpa_tela()

def apresentacao():
    print("""
    █▀▀ █▀█ █▀▄▀█ █▀█   █▀█   █▀▄▀█ █░█ █▄░█ █▀▄ █▀█   ▀█▀ █▀▀   █░█ █▀▀
    █▄▄ █▄█ █░▀░█ █▄█   █▄█   █░▀░█ █▄█ █░▀█ █▄▀ █▄█   ░█░ ██▄   ▀▄▀ ██▄
    """)

def analisa_idade(idade):

    if idade < 0:
        print(f'Idade inválida')
        return 0

    if idade < 13:
        return 'Criança'

    if idade < 19:
        return 'Adocente'

    return 'Adulto'

def main():

    limpa_tela()
    apresentacao()
    idade = int(input('Qual é a sua idade? '))
    print(f'Com a idade de {idade} anos, o mundo te vê como {analisa_idade(idade)}')


if __name__ == '__main__':
    main()