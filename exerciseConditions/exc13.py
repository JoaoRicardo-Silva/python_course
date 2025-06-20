# 13. Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.

def calcular_variacao_percentual(vendas_2022, vendas_2023):
    if vendas_2022 == 0:
        return float('inf')  # Evita divisão por zero
    return ((vendas_2023 - vendas_2022) / vendas_2022) * 100
def analisar_vendas(vendas_2022, vendas_2023):
    variacao = calcular_variacao_percentual(vendas_2022, vendas_2023)
    
    if variacao > 20:
        return "Bonificação para o time de vendas."
    elif 2 < variacao <= 20:
        return "Pequena bonificação para o time de vendas."
    elif -10 < variacao <= 2:
        return "Planejamento de políticas de incentivo às vendas."
    else:
        return "Corte de gastos."
def main():
    try:
        vendas_2022 = float(input("Digite a quantidade de vendas em 2022: "))
        vendas_2023 = float(input("Digite a quantidade de vendas em 2023: "))
    except ValueError:
        print("Valor inválido! Por favor, digite números válidos.")
        return

    resultado = analisar_vendas(vendas_2022, vendas_2023)
    print(resultado)
if __name__ == "__main__":
    main()