# 1. Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print("Os números são iguais.")