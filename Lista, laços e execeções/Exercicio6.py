# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
import os

os.system('cls')

numeros = [1,2,3,'4',5,"p",6,8,5.8]
problemas = []
soma = 0
for x in numeros:
    try:
        soma += x
    except:
        problemas.append(x)
    
print(f'A soma dos elementos é: {soma}')
print(f'Os elementos {problemas}, não foram possível ')