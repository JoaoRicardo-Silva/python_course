#4. Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
temperaturas = []
while True:
    try:
        temperatura = float(input("Digite a temperatura em Celsius (-273 para encerrar):"))
        if temperatura == -273:
            break # Encerra a leitura se o valor for -273
        temperaturas.append(temperatura)  # Adiciona a temperatura à lista
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"A média das temperaturas é {media:.2f}°C.")
else:
    print("Nenhuma temperatura válida foi informada.")

# Teste de execução.