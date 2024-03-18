# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.

# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# # Primeira forma
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [
#         (l1[i], l2[i]) for i in range(intervalo)
#     ]


# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print('\n', zipper(l1, l2), '\n')


# # Segunda forma com zip - (Uma forma menor e mais prática)
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))


# Terceira forma com zip_longest - (Pega a lista maior)
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print('\n', list(zip_longest(l1, l2, fillvalue="Sem cidade")), '\n')
