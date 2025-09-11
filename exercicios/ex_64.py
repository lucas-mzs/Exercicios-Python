# Verifique se 3 números formam um triângulo e diga o tipo.

def verificar_triangulo():
    print('=== Verificador de Triângulo ===')

    a = float(input('Digite o comprimento do 1º lado: '))
    b = float(input('Digite o comprimento do 2º lado: '))
    c = float(input('Digite o comprimento do 3º lado: '))

    if a + b > c and a + c > b and b + c > a:
        print('\n✅ Os lados podem formar um triângulo.')

        if a == b == c:
            print('🔺 Tipo: EQUILÁTERO (todos os lados são iguais).')
        elif a == b or a == c or b == c:
            print('🔺 Tipo: ISÓSCELES (dois lados iguais).')
        else:
            print('🔺 Tipo: ESCALENO (todos os lados diferentes).')
    else:
        print('\n❌ Os lados NÃO podem formar um triângulo.')

verificar_triangulo()