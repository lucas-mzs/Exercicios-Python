# Leia 6 notas e calcule a média, desconsiderando as menores que 4.

def calcular_media():
    notas = []

    for i in range(1, 7):
        nota = float(input(f'Digite a {i}º nota: '))
        if nota >= 4:
            notas.append(nota)

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\n✅ Sua média (desconsiderando notas < 4) foi: {media:.2f}")
    else:
        print("\n⚠️ Nenhuma nota foi considerada, todas foram menores que 4.")

calcular_media()