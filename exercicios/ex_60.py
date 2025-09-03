# Solicite 5 números e informe o maior e o menor valor.

def maior_menor():
    numeros = []

    for i in range(1, 6):
        n = int(input(f'Digite o {i}º número: '))
        numeros.append(n)
    
    maior = max(numeros)
    menor = min(numeros)

    print("\n=== RESULTADO ===")
    print(f"📈 Maior valor digitado: {maior}")
    print(f"📉 Menor valor digitado: {menor}")

maior_menor()