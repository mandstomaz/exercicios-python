par = 0
impar = 0
numTotal = 0
somaTotal = 0
somaPar = 0

num = int(input("Valor: "))

while num > 0:
    somaTotal += num
    numTotal += 1

    if num % 2 == 0:
        par += 1
        somaPar += num
    else:
        impar += 1

    num = int(input("Valor: "))

if numTotal > 0:
    mediaGeral = somaTotal / numTotal
    print(f"Números pares: {par}")
    print(f"Números ímpares: {impar}")
    print(f"Média geral dos números lidos: {mediaGeral}")

    if par > 0:
        mediaPares = somaPar / par
        print(f"Média de números pares: {mediaPares}")
    else:
        print(f"Média de números pares: 0")
else:
    print(f"Nenhum número foi digitado.")

