#Elabore um programa que dada uma distância percorrida (em quilômetros), bem como o total de combustível gasto (em litros), informe o consumo do veículo

distancia = float(input("Insira a distância percorrida (km): "))
combustivel = float(input("Insira o total de combustível gasto (litros): "))

consumo = distancia / combustivel

print("O consumo do veículo foi de: ", consumo)