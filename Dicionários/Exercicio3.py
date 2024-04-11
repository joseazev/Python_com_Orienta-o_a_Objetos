#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros = {'Lista':[x for x in range(1,6)]}
quadrado = [x*x for x in numeros['Lista']]

numeros['quadrados'] = quadrado 

print(numeros)
