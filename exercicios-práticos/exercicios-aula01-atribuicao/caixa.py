#Elabore um programa que faça a simulação de um caixa de uma loja. O usuário deverá digitar o Valor da Compra, o Valor Pago pelo cliente. O programa irá retornar o valor do troco, as cédulas que fazem parte do troco e a quantidade de cada cédula. Para este programa considere as cédulas de R$100, R$50, R$20, R$10, R$5 e R$1 real. Considere a possibilidade de não haver troco.

valor_compra = int(input("Insira o valor da compra: R$"))
valor_pago = int(input("Insira o valor pago: R$"))

valor_troco = valor_pago % valor_compra

cedula_100 = valor_troco // 100
sobra = valor_troco % 100

cedula_50 = sobra // 50
sobra = sobra % 50

cedula_20 = sobra // 20
sobra = sobra % 20

cedula_10 = sobra // 10
sobra = sobra % 10

cedula_5 = sobra // 5
sobra = sobra % 5

cedula_1 = sobra // 1
sobra = sobra % 1

print("Compra: R$", valor_compra)
print("Pagamento: R$", valor_pago)
print("Troco: R$", valor_troco)

print("R$100,00", cedula_100, "células")
print("R$50,00", cedula_50, "células")
print("R$20,00", cedula_20, "células")
print("R$10,00", cedula_10, "células")
print("R$5,00", cedula_5, "células")
print("R$1,00", cedula_1, "células")