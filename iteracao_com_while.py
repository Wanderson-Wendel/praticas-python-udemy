# nome = "Luiz Otávio"

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])
# print()

# nova_string = ""
# nova_string += 'L*u*i*z* *O*t*á*v*i*o*'

nome = "Maria Helena"

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
