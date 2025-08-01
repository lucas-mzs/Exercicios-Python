# Refaça o exercício 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Escolha um número: '))

for i in range(10):
    calculo = num * (i + 1)
    print(f'{num} x {i + 1} = {calculo}')