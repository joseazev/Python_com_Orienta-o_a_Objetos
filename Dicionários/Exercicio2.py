#2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoa ={'nome':'José Francisco Azevedo da Silva',
         'idade':41,
         'cidade':'Duque de Caxias'}

print(pessoa)
print()

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

pessoa['idade'] = 42
print(pessoa)
print()

# Adicione um campo de profissão para essa pessoa;
pessoa['profissão'] = 'Analista de Dados'
print()
print(pessoa)

# Remova um item do dicionário.
pessoa.pop('idade')
print()
print(pessoa)