# Try, except, else e finally

try:
    a = 18
    b = 2
    # print(b[0])
    print('linha 1')
    c = a / b
    print('linha 2')

except ZeroDivisionError as error:
    print('Mensagem:', error) # Divisão por zero

except NameError as error:
    print('Mensagem:', error) # Nome b não está definido

except (TypeError, IndexError) as error:
    print('TypeError + IndexError') # TypeError + IndexError
    print('Mensagem:', error )

except Exception as error:
    print('Mensagem:', error )

else:
    print("Não deu erro..")

finally:
    print("Ainda estou aqui..")
