#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

import os

os.system('cls')

numeros = [x for x in range(1,11)]

soma = 0
for x in numeros:
    if x % 2 == 1:
        soma += x
    
print(f'A soma dos numeros impares é {soma}')