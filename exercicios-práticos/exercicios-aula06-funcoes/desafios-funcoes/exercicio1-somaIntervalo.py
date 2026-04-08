def numIntervalo (num1, num2):
    if num2 < num1:
        aux = num1
        num1 = num2
        num2 = aux
    
    soma = 0
    while num1 <= num2:
        soma += num1
        num1 += 1
    return soma

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

resultado = numIntervalo(n1, n2)

print(f"A soma do intervalo de {n1} e {n2} é {resultado}")