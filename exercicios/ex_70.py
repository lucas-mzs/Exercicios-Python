# Leia dois números e exiba o maior e a diferença entre eles.

def numero_maior_diferente():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if n1 > n2:
        maior = n1
        diferenca = n1 - n2
    else:
        maior = n2
        diferenca = n2 - n1
    
    print(f'O maior número entre esses dois é: {maior}')
    print(f'A diferença entre eles é de: {diferenca}')

numero_maior_diferente()