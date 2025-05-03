# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temperatura_celsius = float(input('Digite a temperatura em Celsius: '))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f'{temperatura_celsius}°C é igual a {temperatura_fahrenheit:.2f}°F')