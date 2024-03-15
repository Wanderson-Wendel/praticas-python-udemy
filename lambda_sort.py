lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduarda', 'sobrenome': 'Moreira'},
]

# Forma sem a função Lambda
def ordena(item):
    return item['nome']

lista.sort(key=ordena)

for item in lista:
    print(item)
print()
# Fim da forma sem Lambda


# Forma com a função Lambda e sort()
lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)

# É como se lambda fosse a 'def..'.
# Não é preciso informar nome para a função, apenas chamar logo o parâmetro 'item'
# e não precisa chamar o return, também, só o que deve ser retornando, no caso, 'item'.

# Fim da forma com a função Lambda e sort()




# Forma com a função Lambda e sorted()
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
# o sobrenome 'miranda' em l2, será retornado no final da organização,
# pois, em python, existe uma tabela unicode para fazer a ordenação por
# letras, existe uma ordem de quais letras vem antes e depois, o que inclui
# a ordenação por maíuculas e minúsculas...

# Fim da forma com a função Lambda e sorted()
