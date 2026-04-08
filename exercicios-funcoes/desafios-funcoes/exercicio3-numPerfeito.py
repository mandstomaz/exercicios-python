def numPerfeito(num):
    contador = 1
    soma = 0
    while contador < num:
        if num % contador == 0:
            soma = soma + contador
        contador += 1
    return soma

valor = int(input("Número: "))

resultado = numPerfeito(valor)

if valor == resultado:
    print("Ele é perfeito!")
else:
    print("Ele não é perfeito.")
    

