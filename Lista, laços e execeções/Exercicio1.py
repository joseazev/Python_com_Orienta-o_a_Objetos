# 1 - Crie uma lista para cada informação a seguir:

# .Lista de números de 1 a 10;
# .Lista com quatro nomes;
# .Lista com o ano que você nasceu e o ano atual.

from os import system
import datetime

system('cls')
def pula_linha():
    print('\n')

lista_de_numeros = [x for x in range(1,11)]

lista_com_quatro_nomes = ['José','Vania','Jovan','Teodoro']

ano_atual = datetime.date.today().strftime("%Y")
ano_nacimento = 1982

lista_anos = [ano_atual,ano_nacimento]

print(lista_de_numeros)
pula_linha()
print(lista_com_quatro_nomes)
pula_linha()
print(lista_anos)
pula_linha()