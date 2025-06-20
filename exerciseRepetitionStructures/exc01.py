# 1. Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1  # Troca os valores se o primeiro for maior
for numero in range(numero1 + 1, numero2):
    print(numero, end=' ')
    