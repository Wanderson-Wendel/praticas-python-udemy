''' Exercício com funções '''

def multiplica(*args):

    ''' Multiplica os args e retorna um valor total. '''

    total = 2
    for numero in args:
        print("\nTotal = ", total, "*", numero)
        total *= numero
        print("Total = ", total)

    return print("\nTotal atualizado = ", total)

multiplica(10, 2, 19, 33, 4)
