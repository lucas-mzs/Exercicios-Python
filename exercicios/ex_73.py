# Calcule os 10 primeiros termos de uma sequência de Fibonacci.

def fibonacci_10():
    termos = [0, 1]
    while len(termos) < 10:
        proximo = termos[-1] + termos[-2]
        termos.append(proximo)
    
    print('Os 10 primeiros termos da sequência de Fibonacci são:')
    print(termos)

fibonacci_10()