''' 
Crie funções que multiplicam, triplicam e quadriplicam
um número recebido como parâmetro
'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar




duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))
