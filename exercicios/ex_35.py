# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
# Três lados formam um triângulo quando a soma de quaisquer dos lados for maior que o terceiro.

def pode_formar_triangulo(a: float, b: float, c: float) -> bool:
    return (
        a + b > c and
        a + c > b and
        b + c > a
    )

def main():
    print('Verificador de Triângulo\n')

    lado_1 = float(input('Digite o comprimento da primeira reta: '))
    lado_2 = float(input('Digite o comprimento da segunda reta: '))
    lado_3 = float(input('Digite o comprimento da terceira reta: '))

    if pode_formar_triangulo(lado_1, lado_2, lado_3):
        print('\n✅ As retas podem formar um triângulo.')
    else:
        print('\n❌ As retas **não** podem formar um triângulo.')

main()