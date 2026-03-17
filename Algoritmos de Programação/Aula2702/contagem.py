#Faça um programa para receber um número inteiro representando segundos e imprimir a quantidade correspondente em horas, minutos e segundos

seg = int(input("Insira o número em segundos: "))

horas = seg // 3600 
sobra = seg % 3600
minutos = sobra // 60
seg = sobra % 60

print(f"A hora é: {horas} horas, {minutos} minutos e {seg} segundos")