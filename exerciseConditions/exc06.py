# 6. Escreva um programa que leia três números e os exiba em ordem decrescente.
numeros = []
for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
numeros.sort(reverse=True)
print("Os números em ordem decrescente são:", numeros)
