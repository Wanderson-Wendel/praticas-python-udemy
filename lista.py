print("Utilizando concatenação")
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(f"LISTA_A: {lista_a} + LISTA_B: {lista_b}:\n\n = LISTA_C: {lista_c}")

print("\n")

print("Utilizando extend")
lista_d = [1,2,3]
print(f"LISTA_D: {lista_d}")

lista_d.extend([4,5,6,7,8,9])
print(f"LISTA_D EXTENDIDA: {lista_d}")
