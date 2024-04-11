#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa ={'nome':'José Francisco Azevedo da Silva',
         'idade':41,
         'cidade':'Duque de Caxias'}

chave = 'idade'

mensagem = f'chave encontrada' if chave in pessoa else f'chave nao encontrada'

print(mensagem)