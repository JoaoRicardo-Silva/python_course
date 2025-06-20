# 10. Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

def verificar_numero(numero):
    if numero.is_integer():
        tipo = "inteiro"
    else:
        tipo = "decimal"

    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    return f"O número {numero} é {tipo}, {sinal} e {paridade}."

def realizar_operacao(num1, num2, operacao):
    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 == 0:
            return "Divisão por zero não é permitida."
        resultado = num1 / num2
    else:
        return "Operação inválida."

    return verificar_numero(resultado)

def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Valor inválido! Por favor, digite números válidos.")
        return

    operacao = input("Qual operação você deseja realizar? (soma, subtracao, multiplicacao, divisao): ").strip().lower()

    resultado = realizar_operacao(num1, num2, operacao)
    print(resultado)

if __name__ == "__main__":
    main()