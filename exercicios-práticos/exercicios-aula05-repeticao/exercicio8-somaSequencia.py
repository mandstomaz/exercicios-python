n = int(input("Valor: "))
ant1 = 3
ant2 = 2
soma = 5

for cont in range(3, n + 1):
    atual = ant1 + ant2
    soma += atual
    ant2 = ant1
    ant1 = atual

print(f"Soma: {soma}")