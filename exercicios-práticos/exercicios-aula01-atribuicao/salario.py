#Leia o salário mensal atual de um funcionário e o percentual de reajuste e determine o valor do novo salário
salario_atual = float(input("Insira o salário atual mensal: R$"))
percentual = float(input("Insira o percentual de reajuste: "))

salario_final = salario_atual + (salario_atual * percentual / 100)

print("O novo salário será de: R$", salario_final)

