# Criando arquivos com Python
# Usamos a função open para abrir um arquivo
# em Python (ele pode ou não existir)

# Modo:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto) + (leitura e escrita)
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever, ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = '/home/wandersonwendel/Documentos/praticas-python-udemy/'
caminho_arquivo += 'arquivos.txt'

# arquivo = open(caminho_arquivo, 'w')

# Sempre que abrir um arquivo, já adicionar o close para evitar problemas
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.writelines(
#         ('linha 3\n', 'linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='') # Removendo as quebras de linha extras
#     print(arquivo.readline().strip()) # Removendo as quebras de linha extras, com strip para string
#     print(arquivo.readline().strip()) # Removendo as quebras de linha extras, com strip para string

#     print("READLINES")
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 20)


# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# "a" seria o modo append (abrir e acrescentar conteúdo a ele, com write)
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )
