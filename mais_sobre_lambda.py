'''Passar estas funções para lambda'''

# Função que irá executar a lambda
def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica



# Função executa() para a função soma()
print(
    executa(
        lambda x,y: x + y, # lambda seria a funcao
        2, 3 # os *args
    )
)
# Fim da função executa()


# Função executa para a função cria_multiplicador()
# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))
# Fim da função executa para a função cria_multiplicador()
