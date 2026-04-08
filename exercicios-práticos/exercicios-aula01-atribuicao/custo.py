#Faça um programa que dadas as medidas de uma sala em metro (comprimento e largura), bem como o preço do metro quadrado do carpete, informe o custo total para forrar o piso da sala

comprimento = float(input("Insira o comprimento da sala (metros): "))
largura = float(input("Insira a largura da sala (metros): "))
carp_metro = float(input("Digite o preço do metro quadrado do carpete: "))

area = comprimento * largura 
valor_final = carp_metro * area

print("O custo total para forrar o piso da sala é: ", valor_final)