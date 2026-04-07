a = int(input("Valor: "))
b = int(input("Valor: "))

def numIntervalo(num1, num2):
    if num2 < num1:
        aux = num1
        num1 = num2
        num2 = aux
    while (num1 <= num2):
        if num1 % 2 == 0:
            print(num1)
            num1 += 2
        else:
            print(num1)
            num1 += 1
    return num1, num2

print(f"a = {a} e b = {b}")

numIntervalo(a, b)