def numFatorial (num):
    contador = 1
    fatorial = 1
    while (contador <= num):
        fatorial *= contador
        contador = contador + 1
    return fatorial

num1 = int(input("Número inteiro: "))
num2 = int(input("Número inteiro: "))
num3 = int(input("Número inteiro: "))

n1 = numFatorial(num1) 
n2 = numFatorial(num2)
n3 = numFatorial(num3)

print(f"Fatorial de {num1}: {n1}")
print(f"Fatorial de {num2}: {n2}")
print(f"Fatorial de {num3}: {n3}")