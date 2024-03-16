# List Compreehension é uma forma rápida
#para criar listas a partir de interáveis

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# print()

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novs_produtos = [
    # produto['nome']
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
# print(novs_produtos)
print(*novs_produtos, sep='\n')


# Filtro de dados em List Comprehension
