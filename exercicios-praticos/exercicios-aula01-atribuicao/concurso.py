#Uma certa importância será dividida entre três ganhadores de um concurso. Sendo que da quantia total: O primeiro ganhador recebera 46%; O segundo recebera 32%; O terceiro recebera o restante; Elabore um programa que dado o valor do concurso em reais ele, calcule e imprima a quantia ganha por cada um dos ganhadores

concurso_valor = float(input("Insira o valor total do concurso: R$ "))

ganhador1 = concurso_valor * (46 / 100)
ganhador2 = concurso_valor * (32 / 100)
ganhador3 = concurso_valor * (22 / 100)

print("O primeiro ganhador ganhará: R$", ganhador1)
print("O segundo ganhador ganhará: R$", ganhador2)
print("O terceiro ganhador ganhará: R$", ganhador3)