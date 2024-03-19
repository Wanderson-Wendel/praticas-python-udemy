def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] > 100

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 1000
# ]

novos_produtos = filter(
    # Fazendo com lambda
    # lambda produto: produto['preco'] >= 100,

    # Fazendo chamando a função externa
    filtrar_preco, # 1º param: Uma função
    produtos # 2º param: Um iterável
)

# Só exibindo todos os produtos, para comparar
print_iter(produtos)

print("Retornando os produtos filtrados:")
print_iter(novos_produtos)
