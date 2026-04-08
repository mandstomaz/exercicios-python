#Leia um número inteiro qualquer e calcule a soma desse número com os seus três consecutivos (o sucessor, o próximo, e o próximo). Construa da maneira mais eficiente possível.

num = int(input("Digite um número inteiro: "))

suc = num + 1
prox1 = suc + 1
prox2 = prox1 + 1

print(f"O número é: {num}")
print(f"Seu sucessor é {suc}, seu próximo é {prox1} e o próximo dele é {prox2}")