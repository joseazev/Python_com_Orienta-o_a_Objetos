#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

import os

def limpa_tela():
    
    os.system('cls')

def apresentacao():

    print("""
    █▀▀   █▀█ ▄▀█ █▀█   █▀█ █░█   █ █▀▄▀█ █▀█ ▄▀█ █▀█ ▀█
    ██▄   █▀▀ █▀█ █▀▄   █▄█ █▄█   █ █░▀░█ █▀▀ █▀█ █▀▄ ░▄
    """)

def analisa_numero(numero):
    return numero%2

def par_ou_impar(numero):
    if analisa_numero(numero):
        print(f'{numero} é numero é impar')
    else:
        print(f'{numero} é numero é par')
 

def main():
    limpa_tela()
    apresentacao()
    numero = int(input('informe o numero que deseha analisar\n'))
    par_ou_impar(numero)


if __name__ == '__main__':
    main()