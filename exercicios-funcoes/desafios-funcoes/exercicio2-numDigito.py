def somaDigito (num):
    soma = 0
    while num > 0:
        digito = num % 10
        soma += digito
        num //= 10
    return soma

def maiorDigito (num):
    maior = 0
    while num > 0:
        digito = num % 10
        if digito > maior:
            maior = digito
        num //= 10
    return maior

n = int(input("Digite um número: "))

resultadoSoma = somaDigito(n)
resultadoMaior = maiorDigito(n)

print(f"A soma dos dígitos de {n} é {resultadoSoma}")
print(f"O maior dígito de {n} é {resultadoMaior}")