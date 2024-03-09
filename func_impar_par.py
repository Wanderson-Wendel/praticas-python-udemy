''' Exercício com Funções '''

def impar_par(numero):
    ''' Saber se é ímpar ou par '''
    multiplo_de_2 = (numero % 2) == 0

    if multiplo_de_2:
        return f'{numero} é par.'

    return f'{numero} é ímpar.'

print(impar_par(2))
print(impar_par(5))
print(impar_par(10))
print(impar_par(1))
