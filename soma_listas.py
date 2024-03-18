'''
Considerando duas listas de inteiros ou floats (lista_a e lista_b)
Some os valores nas listas, retornando uma nova lista com os valores somados
(índice 0 de lista_a + índice 0 de lista_b, e assim sucessivamente):

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Ex.:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

=================> Resultado
lista_soma = [2, 4, 6, 8]
'''



# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = []

# Primeira forma de fazer
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])

# Segunda forma de fazer (com enumerate), mas ainda não é a melhor
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


# Terceira forma de fazer (com zip e list comprehension) bem mais simples
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma  = [x + y for x, y in zip(lista_a, lista_b)]
print(list(zip(lista_a, lista_b))) #- Só para o caso de querer ver como seria a junção das listas
print(lista_soma)


# Quarta forma (com zip_longest)
# from itertools import zip_longest

# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]

# lista_soma  = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(list(zip_longest(lista_a, lista_b, fillvalue=0))) #- Só para o caso de querer ver como seria a junção das listas
# print(lista_soma)
