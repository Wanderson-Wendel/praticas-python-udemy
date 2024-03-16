# isinstance - para saber se um objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    # Saber se o 1º parâmetro é instância do 2º
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))
