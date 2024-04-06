# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo #com as seguintes condições:
#
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

from os import system

system('cls')

def apresentacao():
    print('Batalha Naval')

def descobrindo_quadrante(x,y):
    if x == 0 and y == 0:
        return 0
    
    if x >= 0 and y >= 0:
        return 1
    
    if x <= 0 and y >=0:
        return -1
    
    if x <= 0 and y <=0:
        return 2
    
    if x >= 0 and y <=0:
        return -2


def definindo_quadrante(z):
    if z == 0:
        return f'O ponto está localizado no eixo ou origem'
    
    if z == 1:
        return f'O ponto está no primeiro quadrante'
    
    if z == -1:
        return f'O ponto está no segundo quadrante'
    
    if z == 2:
        return f'O ponto está no terceiro quadrante'
    
    if z == -2:
        return f'O ponto está no quarto quadrante'
    

def main():
    apresentacao()
    x = int(input('Qual é o ponto X? '))
    y = int(input('Qual é o ponto y? '))

    result = definindo_quadrante(descobrindo_quadrante(x,y))
    print(result)

if __name__ == '__main__':
    main()
