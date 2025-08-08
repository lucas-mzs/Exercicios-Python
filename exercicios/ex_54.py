# Some os números divisíveis por 5 entre 1 e 100.

def numeros_divisiveis():
    for i in range(101):
        if i % 5 == 0:
            print(i, end=' ')

numeros_divisiveis()