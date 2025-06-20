#  12. Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

def calcular_valor_pago(quantidade_litros, tipo_combustivel):
    if tipo_combustivel.upper() == 'E':
        preco_por_litro = 1.70
        if quantidade_litros <= 15:
            desconto = 0.02
        else:
            desconto = 0.04
    elif tipo_combustivel.upper() == 'D':
        preco_por_litro = 2.00
        if quantidade_litros <= 15:
            desconto = 0.03
        else:
            desconto = 0.05
    else:
        return "Tipo de combustível inválido."

    valor_total = preco_por_litro * quantidade_litros
    valor_desconto = valor_total * desconto
    valor_a_pagar = valor_total - valor_desconto

    return f"Valor a ser pago: R$ {valor_a_pagar:.2f}"
def main():
    try:
        quantidade_litros = float(input("Digite a quantidade de litros vendidos: "))
        tipo_combustivel = input("Digite o tipo de combustível (E para Etanol, D para Diesel): ")
    except ValueError:
        print("Valor inválido! Por favor, digite números válidos.")
        return

    resultado = calcular_valor_pago(quantidade_litros, tipo_combustivel)
    print(resultado)
if __name__ == "__main__":
    main()