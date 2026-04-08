habitantes = int(input("Quantidade de pessoas na cidade: "))

#------------------PESO----------------
peso = 0
contador = 1

while contador <= habitantes:
    valorPeso = float(input("Insira o peso: "))
    peso = peso + valorPeso
    contador += 1

mediaPeso = peso / habitantes

print(f"A cidade possui {habitantes} habitantes.")
print(f"A média dos pesos dos habitantes é {mediaPeso}")

#--------------------MEDIA DE FILHOS------------------

idadePessoas = int(input("Quantidade de pessoas com idade entre 30 a 40 anos: "))
contador = 1
filhos = 0

while contador <= idadePessoas:
    filhosPessoas = int(input("Insira quantos filhos voce tem: "))
    filhos += filhosPessoas
    contador += 1

mediaFilhos = filhos / idadePessoas

print(f"{idadePessoas} pessoas tem entre 30 a 40 anos")
print(f"A média dos filhos é {mediaFilhos}")