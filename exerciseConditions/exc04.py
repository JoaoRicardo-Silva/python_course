# 4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

valor1 = float(input("Digite o valor médio do carro no primeiro ano:"))
valor2 = float(input("Digite o valor médio o carro no segundo ano: "))
valor3 = float(input("Digite o valor médio do carro no terceiro ano: "))

valores = [valor1, valor2, valor3]
valor_maximo = max(valores)
valor_minimo = min(valores)
print(f"O valor mais alto entre os três anos foi de: {valor_maximo} e o valor mais baixo foi de {valor_minimo}.")
