# Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será 
# formado: todos os lados iguais é EQUILÁTERO; dois lados iguais é ISÓSCELES; todos os lados diferentes é ESCALENO.

def pode_formar_triangulo(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a: float, b: float, c: float) -> str:
    if a == b == c:
        return 'EQUILÁTERO (todos os lados iguais.)'
    elif a == b or a == c or b == c:
        return 'ISÓSCELES (dois lados iguais.)'
    else:
        return 'ESCALENO (todos os lados diferentes.)'

def main():
    print('\n=== Verificador de Triângulo ===\n')

    try:
        lado_1 = float(input('Digite o comprimento da primeira reta: '))
        lado_2 = float(input('Digite o comprimento da segunda reta: '))
        lado_3 = float(input('Digite o comprimento da terceira reta: '))
    except ValueError:
        print('\n❌ Entrada inválida. Por favor, digite valores numéricos.')
        return
    
    if pode_formar_triangulo(lado_1, lado_2, lado_3):
        print('\n✅ As retas podem formar um triângulo.')
        tipo = tipo_triangulo(lado_1, lado_2, lado_3)
        print(f'Tipo de triângulo: {tipo}')
    else:
        print('\n❌ As retas **não** podem formar um triângulo.')

main()