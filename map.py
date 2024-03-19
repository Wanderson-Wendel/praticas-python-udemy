from functools import partial

# map - para mapear dados

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

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# Criando uma função com parcial que executa outra função
aumenta_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem = 1.1
)


# # Utilizando list comprehension
# novos_produtos = [
#     # Espandindo o dicionário com **p
#     {**p,
#     'preco': aumenta_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumenta_dez_porcento(
            produto['preco']
        )
    }

# Utilizando a função map()
novos_produtos = map(
    # Aqui, map passa esta função em cada um dos produtos
    muda_preco_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)


#########################
# Só um exemplo simples de mapear lista com valores triplicados

# Organizando os parâmetros de map()
print(
    list(
        map(
            # O primeiro sempre é uma função
            lambda x: x * 3, # lambda de x, me retorne x * 3

            # Segundo parâmtro são os argumentos que serão usados
            # neste caso, foi uma lista
            [1, 2, 3, 4]
            # Para cada argumento, retorne o argumento * 3
            # Result: [3, 6, 9, 12]
        )
    )
)
