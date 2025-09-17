# Converta um número decimal para binário sem usar bin().

def decimal_para_binario():
    n = int(input('Digite um número decimal: '))
    original = n
    binario = ''

    if n == 0:
        binario = '0'
    else:
        while n > 0:
            resto = n % 2
            binario = str(resto) + binario
            n = n // 2
    
    print(f'O número decimal {original} em binário é: {binario}')

decimal_para_binario()