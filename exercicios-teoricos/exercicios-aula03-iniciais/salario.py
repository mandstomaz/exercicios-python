#Uma empresa paga a seus empregados um salário de R$1.500,00 por mês mais uma comissão de R$200,00 para cada carro vendido e mais 5% do valor da venda. Construir um programa para calcular o salário do mês de um funcionário, de acordo com o descrito acima. Para o cálculo da comissão e do adicional de 5% do valor da venda, o programa deverá ler o número de carros vendidos e valor total das vendas, do empregado, no mês e, imprimir de forma bem explicativa o salário do funcionário:

carros_vendidos = int(input("Digite o número de carros vendidos: "))
vendasTotal = float(input("Digite o valor total das vendas: R$"))

salario = 1500.00
comissao = 200.00
porcentualVendas = 0.05

comissaoTotal = carros_vendidos * comissao
vendasAdicional = vendasTotal * porcentualVendas

salarioFinal = salario + comissaoTotal + vendasAdicional

print(f"Salário base: R$1500.00")
print(f"Número de carros vendidos: {carros_vendidos}")
print(f"Total de vendas: R${vendasTotal:.2f}")
print(f"Total de Comissão: R${comissaoTotal:.2f}")
print(f"Total de Adicional de 5%: R${vendasAdicional:.2f}")
print(f"Salário a receber: R${salarioFinal:.2f}")