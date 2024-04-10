# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

import os

os.system('cls')

print("""

█▀▄▀█ █▀▀ █▀▄ █ ▄▀█ █▀
█░▀░█ ██▄ █▄▀ █ █▀█ ▄█
""")

numeros = numeros = [1,2,3,'4',5,"p",6,8,5.8]
soma = 0
exceto = []
for x in numeros:
    try:
        soma += x
    except:
        exceto.append(x)
    
media = soma/(len(numeros)-len(exceto))

print(f'Lista para calculo {numeros}.\n')
print(f'Soma dos numeros nas listas é {soma}.\n')
print(f'Quantidade de elementos na lista é {len(numeros)}\n')
print(f'A media do numeros da lista é {media}\n')