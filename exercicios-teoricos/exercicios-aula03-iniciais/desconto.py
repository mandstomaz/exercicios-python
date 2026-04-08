#A loja “FiqueFeliz” resolveu liquidar todos os seus produtos, para isso necessita de um programa que ajude calcular os novos preços desses produtos. Elabore um programa que leia o preço de um produto, o valor do desconto (em porcentagem) e calcule o novo preço. Imprimir o valor do produto, o desconto e o novo valor.

preco_antigo = float(input("Digite o valor do produto: R$"))
desconto = int(input("Digite o valor do desconto: "))

preco_novo = preco_antigo * (desconto / 100)

print(f"Preço do produto: R${preco_antigo:.2f}")
print(f"Valor do desconto: {desconto}%")
print(f"Preço do produto com desconto: R${preco_novo:.2f}")