# 2. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = float(input("Digite o percentual de crescimento da produção: "))

if percentual > 0:
    print(f"Houve um crescimento de {percentual}% na produção.")
elif percentual < 0:
    print(f"Houve um descrescimento de {abs(percentual)}% na produção.")
else:
    print("Não houve alterção na produção.")