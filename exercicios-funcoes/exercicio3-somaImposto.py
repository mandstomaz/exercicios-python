def somaImposto(taxaImposto, custo):
    soma = custo + (custo * (taxaImposto / 100))
    return soma

valor = float(input("Valor de custo: "))
taxa = float(input("Valor da taxa de imposto: "))

resultado = somaImposto(taxa, valor)

print(f"Valor do custo: {valor}")
print(f"Valor do custo com taxa de imposto: {resultado}")