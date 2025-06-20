# 9. Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = input("Digite um número:")
try:
    float_num = float(numero)
    if float_num.is_integer():
        print(f"O número {numero} é inteiro.")
    else:
        print(f"O número {numero} é decimal.")
except ValueError:
    print("Valor inválido! Por favor, digite um número válido.")