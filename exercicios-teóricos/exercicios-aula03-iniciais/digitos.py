#Escrever um programa que faz a leitura de um número inteiro de até 2 dígitos e imprima a soma dos dígitos. Considere que somente serão digitados números de 1 ou 2 dígitos.

num = int(input("Digite um número inteiro de até 2 dígitos: "))

div1 = num // 10
resto1 = num % 10
div2 = div1 + resto1

print(f"{div2}")