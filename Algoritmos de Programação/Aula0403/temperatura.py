#Faça um programa que converta uma temperatura em graus Fahrenheit para Celsius. A temperatura em Fahrenheit deverá ser lida do teclado. Utilize a fórmula C = (F - 32) * 5/9, onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

fahren = float(input("Insira a temperatura em Fahrenheit: "))

celsius = (fahren - 32) * 5 / 9

print(f"A temperatura em Fahrenheit é: {fahren}°F")
print(f"Convertendo a temperatura para Celsius fica: {celsius:2.0f}°C")