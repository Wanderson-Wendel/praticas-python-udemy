# def mostrar_args_nomeados(*args, **kwargs):
#     print(kwargs)

# mostrar_args_nomeados(nome="joao", num=1, nom="jo")


def mostrar_args_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS:", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_args_nomeados(1, 2, nome="joao", num=1, nom="jo")
