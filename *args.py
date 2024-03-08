def soma(*args):
    print("Números: ", args)
    
    total = 0
    print("Total: ", total)

    for numero in args:
        print("\nTotal = ", total, "+", numero)
        total += numero
        print("Total = ", total)

    print("\nTotal atualizado = ",total)

soma(1,2,3,4,5,6)
