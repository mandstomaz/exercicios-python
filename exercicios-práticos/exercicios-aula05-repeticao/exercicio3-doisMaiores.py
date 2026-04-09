maior = 0
segundo_maior = 0
contador = 1

while contador <= 10:
    num = int(input("Digite um número: "))
    if num > maior:
        segundo_maior = maior
        maior = num
    else:
        if num > segundo_maior:
            segundo_maior = num
    contador += 1

print(f"Maior: {maior}")
print(f"Segundo maior: {segundo_maior}")