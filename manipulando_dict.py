# Manipulando chaves e valores em dicionários

'''Dicionário vazio'''
pessoa = {}

##
##
'''Criando chave dinâmicamente'''
chave = 'nome'

''' Criando chaves'''
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

'''Acessando a chave pelos colchetes'''
print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome')) # Se não acha, retorna None

print('ISSO NÂO VAI!')
