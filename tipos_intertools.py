from itertools import combinations, permutations, product

def print_inter(interator):
    print(*list(interator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

print("-- COMBINAÇÃO --> ordem não importa - combinações quase que únicas")
print_inter(combinations(pessoas, 2))
print()

print("-- PERMUTAÇÃO --> Ordem importa - combinações iguais")
print_inter(permutations(pessoas, 2))
print()


camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'dryfit', 'poliéster'],
]
print("-- PRODUTO --> ordem importa e repete valores únicos")
print_inter(product(*camisetas))