# 5. Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto:"))
preco3 = float(input("Digite o preço do terceiro produto:"))

precos = [preco1, preco2, preco3]
produto_mais_barato = min(precos)

print(f"O produto mais barato custa: {produto_mais_barato}")