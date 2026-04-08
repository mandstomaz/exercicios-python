def val_int (a, b, c):
    somaTres = a + b + c
    return somaTres

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = int(input("Digite um número inteiro: "))

resultado = val_int(num1, num2, num3)

print(f"{num1} + {num2} + {num3} = {resultado}")