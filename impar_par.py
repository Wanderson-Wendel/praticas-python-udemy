"""
Faça um programa que peça ao usuário para digitar um número inteiro e
informar se este número é impar ou par. Caso o usuário digite um número
que não seja inteiro, informe que não é inteiro.
"""

entrada = input("Digite um número: ")

# Primeira Forma:
# entrada_int = int(entrada)
#
# if entrada.isdigit():
#    par_impar = entrada_int % 2 == 0
#    par_impar_texto = 'ímpar'
#
#    if par_impar:
#        par_impar_texto = 'par'
#    
#    print(f"O número {entrada_int} é {par_impar_texto}.")
#else:
#    print("Você não digitou um número inteiro!") """



# Segunda Forma
entrada_int = float(entrada)

try:
   par_impar = entrada_int % 2 == 0
   par_impar_texto = 'ímpar'

   if par_impar:
       par_impar_texto = 'par'
   
   print(f"O número {entrada_int} é {par_impar_texto}.")
except:
   print("Você não digitou um número inteiro!")
