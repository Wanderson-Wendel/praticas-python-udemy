import copy
from dados import produtos

# copy, sorted, produtos.sort
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    # Gerando dict com chave preco com valor aumentado.
    # Round para ditar casas decimais mínimas
    {**p, 'preco': round(p['preco'] * 1.1, 2)}

    # List Comprehension - Mapeamento de um produto p/ outro produto
    for p in copy.deepcopy(produtos)

]

# Ordene os produtos por nome decrescente
# Gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = sorted(
    # Criando copy.deepcopy
    copy.deepcopy(produtos),

    # Função pra retornar produtos por nome decrescente
    key=lambda p: p['nome'],
    reverse=True
)


# Ordene os produtos por preco crescente
#Gere produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),

    # Função pra retornar produtos por preço crescente
    key=lambda p: p['preco']
)


# Resultados

print("\nProdutos originais --", *produtos, sep='\n')
print()
print("Aumento dos preços dos produtos em 10% --", *novos_produtos, sep='\n')
print()
print("Produtos ordenados por nome decrescente --", *produtos_ordenados_por_nome, sep='\n')
print()
print("Produtos ordenados por preco crescente --", *produtos_ordenados_por_preco, sep='\n')
